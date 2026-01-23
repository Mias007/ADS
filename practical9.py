# ============================================
# KMP STRING MATCHING (PRE-DEFINED TEXT)
# ============================================

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    positions = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    text = (
        "Knuth Morris Pratt algorithm is efficient. "
        "The KMP algorithm avoids unnecessary comparisons "
        "in string matching."
    )

    print("Text:")
    print(text)

    pattern = input("\nEnter pattern to search: ")

    result = kmp_search(text, pattern)

    if result:
        print("Pattern found at positions:", result)
    else:
        print("Pattern not found")
