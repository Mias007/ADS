# ============================================
# 2–3 TREE IMPLEMENTATION
# ============================================

class TwoThreeNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0


class TwoThreeTree:
    def __init__(self):
        self.root = None

    # ---------- Insert ----------
    def insert(self, key):
        if not self.root:
            self.root = TwoThreeNode([key])
        else:
            new_root = self._insert(self.root, key)
            if isinstance(new_root, tuple):
                self.root = TwoThreeNode(
                    [new_root[1]],
                    [new_root[0], new_root[2]]
                )
            else:
                self.root = new_root

    def _insert(self, node, key):
        if node.is_leaf():
            node.keys.append(key)
            node.keys.sort()
        else:
            if key < node.keys[0]:
                child = self._insert(node.children[0], key)
            elif len(node.keys) == 1 or key < node.keys[1]:
                child = self._insert(node.children[1], key)
            else:
                child = self._insert(node.children[2], key)

            if isinstance(child, tuple):
                left, median, right = child
                self._add_child(node, median, left, right)

        if len(node.keys) == 3:
            return self._split(node)

        return node

    # ---------- Add Child ----------
    def _add_child(self, node, key, left, right):
        node.keys.append(key)
        node.keys.sort()
        pos = node.keys.index(key)
        node.children.pop(pos)
        node.children.insert(pos, left)
        node.children.insert(pos + 1, right)

    # ---------- Split Node ----------
    def _split(self, node):
        mid_key = node.keys[1]

        left = TwoThreeNode(
            [node.keys[0]],
            node.children[:2]
        )
        right = TwoThreeNode(
            [node.keys[2]],
            node.children[2:]
        )

        return (left, mid_key, right)

    # ---------- Inorder Traversal ----------
    def inorder(self, node):
        if node:
            if node.is_leaf():
                for k in node.keys:
                    print(k, end=" ")
            else:
                for i, k in enumerate(node.keys):
                    self.inorder(node.children[i])
                    print(k, end=" ")
                self.inorder(node.children[-1])


# ============================================
# DRIVER CODE
# ============================================

if __name__ == "__main__":
    tree = TwoThreeTree()
    values = [10, 20, 5, 15, 25, 30]

    for v in values:
        tree.insert(v)

    print("Inorder Traversal of 2–3 Tree:")
    tree.inorder(tree.root)
