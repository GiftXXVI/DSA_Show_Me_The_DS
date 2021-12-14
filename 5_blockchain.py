import hashlib
import random
from datetime import datetime


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
        return f'<--\n Timestamp: {self.timestamp}, \n Data: {self.data}, \n SHA 256 Hash: {self.hash}, \n Prev_Hash: {self.previous_hash} \n-->'


class Blockchain(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data):
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


blockchain = Blockchain()
sample = 'abcdefghijklmnopqrstuvwxyz'
length = 20
strings = [None for i in range(length)]

for i in range(length):
    strings[i] = ''.join(random.choice(sample) for i in range(length))

for string in strings:
    blockchain.insert(string)

blockchain.traverse()
