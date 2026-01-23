# ============================================
# ONE-DIMENSIONAL RANGE SEARCHING
# ============================================

def one_d_range_search(arr, low, high):
    result = []
    for x in arr:
        if low <= x <= high:
            result.append(x)
    return result


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    data = [5, 3, 9, 1, 12, 7, 4, 10]

    print("Data:", data)

    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))

    result = one_d_range_search(data, low, high)

    print("Elements in range:", result)
