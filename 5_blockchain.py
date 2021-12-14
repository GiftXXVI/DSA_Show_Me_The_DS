import hashlib


def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None


class Blockchain(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, block):
          if self.head is None:
                block.previous_hash = 0
                self.head = block
                self.tail = self.head
