# ============================================
# AVL TREE IMPLEMENTATION
# ============================================

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    # ---------- Get Height ----------
    def get_height(self, root):
        return root.height if root else 0

    # ---------- Get Balance Factor ----------
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # ---------- Right Rotation ----------
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                          self.get_height(x.right))

        return x

    # ---------- Left Rotation ----------
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left),
                          self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),
                          self.get_height(y.right))

        return y

    # ===================================
    # INSERT OPERATION
    # ===================================

    def insert(self, root, key):

        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------- Minimum Value Node ----------
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    # ===================================
    # DELETE OPERATION
    # ===================================

    def delete(self, root, key):

        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------- Inorder Traversal ----------
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# ============================================
# DRIVER CODE
# ============================================

if __name__ == "__main__":
    avl = AVLTree()
    root = None

    values = [30, 20, 40, 10, 25]

    for val in values:
        root = avl.insert(root, val)

    print("Inorder traversal after insertion:")
    avl.inorder(root)

    root = avl.delete(root, 20)

    print("\n\nInorder traversal after deletion of 20:")
    avl.inorder(root)
