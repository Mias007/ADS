# ============================================
# B TREE IMPLEMENTATION (MIN DEGREE t = 2)
# ============================================

class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, True)

    # ---------- Traverse ----------
    def traverse(self, node):
        i = 0
        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self.traverse(node.children[i + 1])

    # ---------- Search ----------
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(node.children[i], key)

    # ---------- Insert ----------
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

# ============================================
# DRIVER CODE
# ============================================

if __name__ == "__main__":
    btree = BTree(2)
    values = [10, 20, 5, 6, 12, 30, 7, 17]

    for v in values:
        btree.insert(v)

    print("Traversal of B-Tree:")
    btree.traverse(btree.root)

    print("\n\nSearch 12:", btree.search(btree.root, 12))
    print("Search 50:", btree.search(btree.root, 50))
