# ============================================
# BOYER-MOORE STRING MATCHING (NO FILE INPUT)
# ============================================

NO_OF_CHARS = 256

def bad_character_heuristic(pattern):
    bad_char = [-1] * NO_OF_CHARS
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    bad_char = bad_character_heuristic(pattern)
    positions = []

    shift = 0
    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            positions.append(shift)
            shift += (m - bad_char[ord(text[shift + m])] if shift + m < n else 1)
        else:
            shift += max(1, j - bad_char[ord(text[shift + j])])

    return positions


# ============================================
# MAIN DRIVER
# ============================================

if __name__ == "__main__":
    text = (
        "Boyer Moore algorithm is efficient. "
        "This algorithm is faster than naive string matching."
    )

    print("Text:")
    print(text)

    pattern = input("\nEnter pattern to search: ")

    result = boyer_moore_search(text, pattern)

    if result:
        print("Pattern found at positions:", result)
    else:
        print("Pattern not found")
