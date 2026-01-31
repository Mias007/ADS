# ============================================
# TWO-DIMENSIONAL RANGE SEARCHING
# ============================================

def two_d_range_search(points, x_min, x_max, y_min, y_max):
    result = []
    for (x, y) in points:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            result.append((x, y))
    return result


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

    print("Points:", points)

    x_min = int(input("Enter x_min: "))
    x_max = int(input("Enter x_max: "))
    y_min = int(input("Enter y_min: "))
    y_max = int(input("Enter y_max: "))

    result = two_d_range_search(points, x_min, x_max, y_min, y_max)

    print("Points in range:", result)
