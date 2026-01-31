# Binary Search Tree Implementation with Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---------- Insert ----------
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)

        return root

    # =================================================
    # RECURSIVE TRAVERSALS
    # =================================================

    def inorder_recursive(self, root):
        if root:
            self.inorder_recursive(root.left)
            print(root.data, end=" ")
            self.inorder_recursive(root.right)

    def preorder_recursive(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)

    def postorder_recursive(self, root):
        if root:
            self.postorder_recursive(root.left)
            self.postorder_recursive(root.right)
            print(root.data, end=" ")

    # =================================================
    # NON-RECURSIVE TRAVERSALS
    # =================================================

    # ---------- Inorder ----------
    def inorder_non_recursive(self):
        stack = []
        curr = self.root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right

    # ---------- Preorder ----------
    def preorder_non_recursive(self):
        if not self.root:
            return

        stack = [self.root]

        while stack:
            curr = stack.pop()
            print(curr.data, end=" ")

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    # ---------- Postorder ----------
    def postorder_non_recursive(self):
        if not self.root:
            return

        stack1 = [self.root]
        stack2 = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)

        while stack2:
            print(stack2.pop().data, end=" ")


# =================================================
# DRIVER CODE
# =================================================

if __name__ == "__main__":
    bst = BST()

    n = int(input("Enter number of nodes: "))
    print("Enter values:")
    for _ in range(n):
        bst.insert(int(input()))

    print("\nRecursive Traversals")
    print("Inorder   :", end=" ")
    bst.inorder_recursive(bst.root)

    print("\nPreorder  :", end=" ")
    bst.preorder_recursive(bst.root)

    print("\nPostorder :", end=" ")
    bst.postorder_recursive(bst.root)

    print("\n\nNon-Recursive Traversals")
    print("Inorder   :", end=" ")
    bst.inorder_non_recursive()

    print("\nPreorder  :", end=" ")
    bst.preorder_non_recursive()

    print("\nPostorder :", end=" ")
    bst.postorder_non_recursive()
