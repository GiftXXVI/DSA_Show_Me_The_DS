import hashlib
import random
from datetime import datetime
import unittest


def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = f'{self.data}{self.timestamp}{self.previous_hash}'.encode(
        'utf-8')

    sha.update(hash_str)

    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.calc_hash = calc_hash
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self)
        self.next = None

    def __repr__(self) -> str:
        dt = datetime.utcfromtimestamp(self.timestamp)
        return f'Timestamp: {dt.strftime("%H:%M %d/%m/%Y")}, \n Data: {self.data}, \n SHA 256 Hash: {self.hash}, \n Prev_Hash: {self.previous_hash} \n -->'


class Blockchain(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data):
        if data is not None:
            dt = datetime.now()
            timestamp = datetime.timestamp(dt)
            if self.head is None:
                block = Block(timestamp=timestamp, data=data, previous_hash=0)
                self.head = block
                self.tail = self.head
            else:
                block = Block(timestamp=timestamp, data=data,
                              previous_hash=self.tail.hash)
                self.tail.next = block
                self.tail = self.tail.next

    def traverse(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    def count(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
        self.empty = Blockchain()
        self.null = Blockchain()
        sample = 'abcdefghijklmnopqrstuvwxyz'
        self.length = 20
        self.null_list = [None for i in range(self.length)]
        self.strings = [None for i in range(self.length)]
        for i in range(self.length):
            self.strings[i] = ''.join(random.choice(sample)
                                      for i in range(self.length))
        for string in self.strings:
            self.blockchain.insert(string)

    def test_build(self):
        self.assertEqual(self.blockchain.count(), self.length)

    def test_empty(self):
        self.assertEqual(self.empty.count(), 0)

    def test_null(self):
        for item in self.null_list:
            self.null.insert(item)
        self.null.traverse()
        self.assertEqual(self.null.count(), 0)


if __name__ == "__main__":
    unittest.main()
    pass
