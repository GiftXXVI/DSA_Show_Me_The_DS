import random
from math import ceil
import unittest


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self) -> str:
        return f'Name: {self.name} Grp: {self.groups}, Usr: {self.users}\n'


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is not None and group is not None:
        return _in_group(user, group)
    return False


def _in_group(user, group):
    users = group.get_users()
    users.sort()
    groups = group.get_groups()
    start = 0
    end = len(users) - 1
    mid = ceil((start + end)/2)
    while start <= end:
        if user == users[mid]:
            return True
        elif user < users[mid]:
            end = mid - 1
            mid = ceil((start + end)/2)
        elif user > users[mid]:
            start = mid + 1
            mid = ceil((start + end)/2)
    for grp in groups:
        return _in_group(user, grp)
    return False


class Test(unittest.TestCase):

    def setUp(self):
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("subchild")
        self.none = None
        self.empty = Group('Empty')

    def test_find(self):
        sub_child_user = "sub_child_user"
        self.sub_child.add_user(sub_child_user)
        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)

        sample = 'abcdefghijklmnopqrstuvwxyz'
        length = 20
        strings = [None for i in range(length)]

        for i in range(length):
            strings[i] = ''.join(random.choice(sample) for i in range(length))

        for i in range(len(strings)):
            flag = random.randint(1, 3)
            if flag == 1:
                self.parent.add_user(strings.pop())
            elif flag == 2:
                self.child.add_user(strings.pop())
            else:
                self.sub_child.add_user(strings.pop())
        self.assertTrue(is_user_in_group(sub_child_user, self.parent))
        self.assertFalse(is_user_in_group('nothing', self.parent))

    def test_null(self):
        self.assertEqual(is_user_in_group('user', self.none), False)

    def test_empty(self):
        self.assertEqual(is_user_in_group('user', self.empty), False)

    def test_not_found(self):
        sample = 'abcdefghijklmnopqrstuvwxyz'
        length = 20
        strings = [None for i in range(length)]
        for i in range(length):
            strings[i] = ''.join(random.choice(sample) for i in range(length))

        for i in range(len(strings)):
            flag = random.randint(1, 3)
            if flag == 1:
                self.parent.add_user(strings.pop())
            elif flag == 2:
                self.child.add_user(strings.pop())
            else:
                self.sub_child.add_user(strings.pop())
        self.assertEqual(is_user_in_group("", self.parent),False)

    def test_none(self):
        sample = 'abcdefghijklmnopqrstuvwxyz'
        length = 20
        strings = [None for i in range(length)]
        for i in range(length):
            strings[i] = ''.join(random.choice(sample) for i in range(length))

        for i in range(len(strings)):
            flag = random.randint(1, 3)
            if flag == 1:
                self.parent.add_user(strings.pop())
            elif flag == 2:
                self.child.add_user(strings.pop())
            else:
                self.sub_child.add_user(strings.pop())
        self.assertEqual(is_user_in_group(None, self.parent),False)


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    sample = 'abcdefghijklmnopqrstuvwxyz'
    length = 20
    strings = [None for i in range(length)]
    for i in range(length):
        strings[i] = ''.join(random.choice(sample) for i in range(length))

    for i in range(len(strings)):
        flag = random.randint(1, 3)
        if flag == 1:
            parent.add_user(strings.pop())
        elif flag == 2:
            child.add_user(strings.pop())
        else:
            sub_child.add_user(strings.pop())
    print(is_user_in_group(sub_child_user, parent))
    unittest.main()
