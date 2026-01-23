# ============================================
# RED-BLACK TREE IMPLEMENTATION
# ============================================

RED = True
BLACK = False


class Node:
    def __init__(self, data):
        self.data = data
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = BLACK
        self.root = self.NIL

    # ---------- Left Rotate ----------
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # ---------- Right Rotate ----------
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # ---------- Insert ----------
    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        curr = self.root

        while curr != self.NIL:
            parent = curr
            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.color = RED
        self.fix_insert(node)

    # ---------- Fix Violations ----------
    def fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # Uncle
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)

        self.root.color = BLACK

    # ---------- Inorder Traversal ----------
    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            color = "R" if node.color else "B"
            print(f"{node.data}({color})", end=" ")
            self.inorder(node.right)


# ============================================
# DRIVER CODE
# ============================================

if __name__ == "__main__":
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25, 5]

    for v in values:
        rbt.insert(v)

    print("Inorder traversal of Red-Black Tree:")
    rbt.inorder(rbt.root)
