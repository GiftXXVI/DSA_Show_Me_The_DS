import sys


class Node(object):
    def __init__(self, character=None, frequency=None) -> None:
        self.character = character
        self.frequency = frequency


class MinHeap(object):
    def __init__(self, character, frequency) -> None:
        self.heap = list()

    def get_index(self, index):
        return index - 1

    def get_left_index(self, index):
        return 2*self.get_index(index)

    def get_right_index(self, index):
        return 2*self.get_index(index)+1

    def find_min(self):
        return self.heap[self.get_index(1)]

    def insert(self, node):
        pass

    def extract_min(self):
        pass

    def replace(self, node):
        pass

    def get_size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def __repr__(self) -> str:
        return str(self.heap)

    def __str__(self) -> str:
        return str(self.heap)


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
