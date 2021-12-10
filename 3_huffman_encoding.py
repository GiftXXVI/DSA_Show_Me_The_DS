import sys


class Node(object):
    def __init__(self, character=None, frequency=None) -> None:
        self.character = character
        self.frequency = frequency

    def __repr__(self) -> str:
        return f'({self.character}, {self.frequency})'

    def __str__(self) -> str:
        return f'({self.character}, {self.frequency})'


class MinHeap(object):
    def __init__(self, size) -> None:
        self.heap = [None for i in range(size)]
        self.size = 0

    def extend(self):
        length = len(self.heap)
        arr = [self.heap[i] for i in range(length)]
        self.heap = [None for i in range(2*length)]
        for i in range(length):
            self.heap[i] = arr[i]

    def get_parent(self, index) -> tuple:
        parent_index = index//2
        return self.heap[parent_index], parent_index

    def get_left_child(self, index) -> tuple:
        left_index = 2*index
        return self.heap[left_index], left_index

    def has_left_child(self, index) -> bool:
        left_index = 2*index
        if self.size < left_index and self.heap[left_index] is not None:
            return True
        return False

    def get_right_child(self, index) -> tuple:
        right_index = 2*index+1
        return self.heap[right_index], right_index

    def has_right_child(self, index) -> bool:
        right_index = 2*index+1
        if self.size < right_index and self.heap[right_index] is not None:
            return True
        return False

    def find_min(self) -> Node:
        return self.heap[1]

    def insert(self, node) -> None:
        print(f'Entry: {node}, {self.size}, {len(self.heap)-1}')
        if self.size == 0:
            self.heap[1] = node
            self.size = 1
            print(f'Exit: {node}, {self.size}, {len(self.heap)-1}')
            return
        index = self.size + 1
        self.heap[index] = node
        parent, parent_index = self.get_parent(index)
        while node.frequency < parent.frequency:
            temp = parent
            self.heap[parent_index] = node
            self.heap[index] = parent
            index = parent_index
            if parent_index > 1:
                parent, parent_index = self.get_parent(index)
            else:
                break
        self.size += 1
        if self.size == len(self.heap) - 1:
            self.extend()
        print(f'Exit: {node}, {self.size}, {len(self.heap)-1}')
        return

    def heapify(self, index):
        self._heapify(index)

    def _heapify(self, index):
        if self.has_left_child(index):
            #heapify left
            left, left_index = self.get_left_child(index)
            pass

        if self.has_right_child(index):
            #heapify right
            pass

    def extract_min(self) -> Node:
        node = self.find_min()
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.heapify(1)
        return node

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
    #codes = {}

    #a_great_sentence = "The bird is the word"

    # print("The size of the data is: {}\n".format(
    #    sys.getsizeof(a_great_sentence)))
    #print("The content of the data is: {}\n".format(a_great_sentence))

    #encoded_data, tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(
    #    sys.getsizeof(int(encoded_data, base=2))))
    #print("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    # print("The size of the decoded data is: {}\n".format(
    #    sys.getsizeof(decoded_data)))
    #print("The content of the encoded data is: {}\n".format(decoded_data))

    test_scenario = [('A', 7), ('B', 3), ('C', 7), ('D', 2), ('E', 6)]
    heap = MinHeap(len(test_scenario)+2)
    for item in test_scenario:
        heap.insert(Node(item[0], item[1]))
    print(heap)
