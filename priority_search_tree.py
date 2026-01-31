# ============================================
# PRIORITY SEARCH TREE IMPLEMENTATION
# ============================================

class PSTNode:
    def __init__(self, point):
        self.point = point      # (x, y)
        self.left = None
        self.right = None


class PrioritySearchTree:
    def __init__(self):
        self.root = None

    # ----------------------------------------
    # INSERT OPERATION
    # ----------------------------------------
    def insert(self, root, point):
        if root is None:
            return PSTNode(point)

        # Priority based on y (max heap)
        if point[1] > root.point[1]:
            point, root.point = root.point, point

        # BST property based on x
        if point[0] < root.point[0]:
            root.left = self.insert(root.left, point)
        else:
            root.right = self.insert(root.right, point)

        return root

    def insert_point(self, point):
        self.root = self.insert(self.root, point)

    # ----------------------------------------
    # RANGE SEARCH OPERATION
    # Search for points where:
    # x_min ≤ x ≤ x_max and y ≥ y_min
    # ----------------------------------------
    def range_search(self, root, x_min, x_max, y_min, result):
        if root is None:
            return

        x, y = root.point

        if x_min <= x <= x_max and y >= y_min:
            result.append((x, y))

        if root.left and x_min <= x:
            self.range_search(root.left, x_min, x_max, y_min, result)

        if root.right and x <= x_max:
            self.range_search(root.right, x_min, x_max, y_min, result)

    def search(self, x_min, x_max, y_min):
        result = []
        self.range_search(self.root, x_min, x_max, y_min, result)
        return result


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    pst = PrioritySearchTree()

    points = [(5, 20), (3, 15), (8, 25), (2, 10), (6, 18), (9, 5)]

    print("Inserting points:")
    for p in points:
        print(p)
        pst.insert_point(p)

    x_min = 3
    x_max = 8
    y_min = 15

    print("\nSearching points in range:")
    print(f"x in [{x_min}, {x_max}] and y ≥ {y_min}")

    result = pst.search(x_min, x_max, y_min)
    print("Result:", result)
