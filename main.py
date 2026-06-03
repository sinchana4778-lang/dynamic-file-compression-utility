

import heapq
import os
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:

    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}

    def build_frequency_table(self, text):
        return Counter(text)

    def build_heap(self, frequency):
        heap = []

        for char, freq in frequency.items():
            heapq.heappush(heap, Node(char, freq))

        return heap

    def build_huffman_tree(self, heap):

        while len(heap) > 1:

            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)

            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]

    def generate_codes(self, root, current_code=""):

        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_codes[current_code] = root.char
            return

        self.generate_codes(root.left, current_code + "0")
        self.generate_codes(root.right, current_code + "1")

    def compress(self, text):

        encoded_text = ""

        for char in text:
            encoded_text += self.codes[char]

        return encoded_text

    def decompress(self, encoded_text):

        current_code = ""
        decoded_text = ""

        for bit in encoded_text:

            current_code += bit

            if current_code in self.reverse_codes:
                decoded_text += self.reverse_codes[current_code]
                current_code = ""

        return decoded_text


def compression_ratio(original_size, compressed_size):

    return round((compressed_size / original_size) * 100, 2)


def main():

    file_path = "input_files/sample.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    huffman = HuffmanCoding()

    frequency = huffman.build_frequency_table(text)

    print("\nFrequency Table:\n")
    print(frequency)

    heap = huffman.build_heap(frequency)

    root = huffman.build_huffman_tree(heap)

    huffman.generate_codes(root)

    print("\nHuffman Codes:\n")

    for char, code in huffman.codes.items():
        print(repr(char), ":", code)

    compressed = huffman.compress(text)

    os.makedirs("compressed_files", exist_ok=True)

    with open("compressed_files/compressed.bin", "w") as file:
        file.write(compressed)

    decompressed = huffman.decompress(compressed)

    os.makedirs("decompressed_files", exist_ok=True)

    with open("decompressed_files/output.txt", "w",
              encoding="utf-8") as file:
        file.write(decompressed)

    original_size = len(text) * 8
    compressed_size = len(compressed)

    ratio = compression_ratio(original_size, compressed_size)

    print("\nCompression Statistics")
    print("----------------------")
    print("Original Size :", original_size, "bits")
    print("Compressed Size :", compressed_size, "bits")
    print("Compression Ratio :", ratio, "%")

    print("\nVerification:")
    print(text == decompressed)


if __name__ == "__main__":
    main()