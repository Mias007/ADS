# ============================================
# HUFFMAN CODING IMPLEMENTATION
# ============================================

import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)

    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)


def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)

    encoded_text = "".join(codes[char] for char in text)
    return codes, encoded_text


# ============================================
# MAIN PROGRAM WITH EXAMPLE
# ============================================

if __name__ == "__main__":
    text = "huffman coding example"

    print("Original Text:")
    print(text)

    codes, encoded_text = huffman_encoding(text)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(f"'{char}' : {code}")

    print("\nEncoded Text:")
    print(encoded_text)
