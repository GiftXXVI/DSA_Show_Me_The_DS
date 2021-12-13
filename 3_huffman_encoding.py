import sys


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item)
                                              for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


class Node(object):
    def __init__(self, character=None, frequency=None, left=None, right=None, bit=None) -> None:
        self.character = character
        self.frequency = frequency
        self.bit = bit
        self.left = left
        self.right = right

    def set_bit(self, bit) -> None:
        self.bit = bit

    def get_bit(self) -> bool:
        return self.bit

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left is not None

    def get_right_child(self):
        return self.right

    def has_right_child(self):
        return self.right is not None

    def __repr__(self) -> str:
        return f'({self.character}, {self.frequency})'

    def __str__(self) -> str:
        return f'({self.character}, {self.frequency})'


class HuffmanTree(object):
    def __init__(self, node) -> None:
        self.root = node

    def get_root(self) -> Node:
        return self.root


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
        if self.heap[left_index] is not None:
            return True
        return False

    def get_right_child(self, index) -> tuple:
        right_index = 2*index+1
        return self.heap[right_index], right_index

    def has_right_child(self, index) -> bool:
        right_index = 2*index+1
        if self.heap[right_index] is not None:
            return True
        return False

    def find_min(self) -> Node:
        return self.heap[1]

    def insert(self, node) -> None:
        if self.size == 0:
            self.heap[1] = node
            self.size = 1
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
        return

    def heapify(self, index):
        self._heapify(index)

    def _heapify(self, index):
        if self.heap[index] is not None:
            if self.has_left_child(index):
                left, left_index = self.get_left_child(index)
                if self.heap[index].frequency > left.frequency:
                    temp = self.heap[index]
                    self.heap[index] = left
                    self.heap[left_index] = temp
                    self._heapify(left_index)

            if self.has_right_child(index):
                right, right_index = self.get_right_child(index)
                if self.heap[index].frequency > right.frequency:
                    temp = self.heap[index]
                    self.heap[index] = right
                    self.heap[right_index] = temp
                    self._heapify(right_index)

        return

    def extract_min(self) -> Node:
        node = self.find_min()
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.heapify(1)
        self.size -= 1
        return node

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def __repr__(self) -> str:
        return str(self.heap)

    def __str__(self) -> str:
        return str(self.heap)


def prepare_string(data):
    frequencies = dict()
    for i in data:
        if i in frequencies:
            frequencies[i] += 1
            continue
        frequencies[i] = 1

    return zip(frequencies.keys(), frequencies.values())


traversal = list()


def pre_order(tree):
    node = tree.root
    binary_str = ''
    traverse(node, binary_str)


def traverse(node, binary_str):
    traversal.append((node, binary_str))
    if node.has_left_child():
        binary_str += '0'
        traverse(node.left, binary_str)
    if node.has_right_child():
        binary_str = binary_str[:-1]
        binary_str += '1'
        traverse(node.right, binary_str)
    return


def huffman_encoding(data):
    prepared_data = list(prepare_string(data))
    heap = MinHeap(len(prepared_data)+2)
    for item in prepared_data:
        heap.insert(Node(item[0], item[1]))

    while(heap.find_min() and heap.get_size() > 2):
        node1 = heap.extract_min()
        node2 = heap.extract_min()
        node1.set_bit(0)
        node2.set_bit(1)
        merge = Node(frequency=node1.frequency +
                     node2.frequency, left=node1, right=node2)
        heap.insert(merge)

    left = heap.extract_min()
    right = heap.extract_min()
    left.set_bit(0)
    right.set_bit(1)
    tree = HuffmanTree(Node(frequency=left.frequency +
                       right.frequency, left=left, right=right))
    encoded_data = ''
    pre_order(tree)
    for chr in data:
        for item in traversal:
            if chr==item[0].character:
                encoded_data += item[1]
    encoded_data
    return encoded_data, tree


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    #codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    # print("The size of the decoded data is: {}\n".format(
    #    sys.getsizeof(decoded_data)))
    #print("The content of the encoded data is: {}\n".format(decoded_data))
