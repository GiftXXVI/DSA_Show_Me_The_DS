from typing import Union
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    node2 = llist_2.head
    union = dict()
    while (node1 is not None) or (node2 is not None):
        if node1 is not None:
            if node1.value not in union:
                union[node1.value] = node1.value
            node1 = node1.next

        if node2 is not None:
            if node2.value not in union:
                union[node2.value] = node2.value
            node2 = node2.next

    return union.keys()


def intersection(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    node2 = llist_2.head
    intersection = dict()
    dict1 = dict()
    dict2 = dict()
    while(node1 is not None) or (node2 is not None):
        if node1 is not None:
            if node1.value not in dict1:
                dict1[node1.value] = node1.value
            node1 = node1.next

        if node2 is not None:
            if node2.value not in dict2:
                dict2[node2.value] = node2.value
            node2 = node2.next

    node1 = llist_1.head
    node2 = llist_2.head

    while (node1 is not None) or (node2 is not None):
        if node1 is not None:
            if node1.value in dict1 and node1.value in dict2:
                intersection[node1.value] = node1.value
            node1 = node1.next
        if node2 is not None:
            if node2.value in dict1 and node2.value in dict2:
                intersection[node2.value] = node2.value
            node2 = node2.next

    return intersection.keys()


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


class Test(unittest.TestCase):
    def setUp(self):
        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()
        self.element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        self.element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in self.element_1:
            self.linked_list_1.append(i)

        for i in self.element_2:
            self.linked_list_2.append(i)

        self.linked_list_3 = LinkedList()
        self.linked_list_4 = LinkedList()
        self.element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        self.element_4 = [1, 7, 8, 9, 11, 21, 1]
        for i in self.element_3:
            self.linked_list_3.append(i)

        for i in self.element_4:
            self.linked_list_4.append(i)

        self.nones = [None for i in range(2)]
        self.linked_list_n1 = LinkedList()
        self.linked_list_n2 = LinkedList()
        for item in self.nones:
            self.linked_list_n1.append(item)
            self.linked_list_n2.append(item)

        self.linked_list_e1 = LinkedList()
        self.linked_list_e2 = LinkedList()

    def test_ui_1(self):

        set_1 = set(self.element_1)
        set_2 = set(self.element_2)
        union_1 = set_1.union(set_2)
        fn_union_1 = set(
            union(self.linked_list_1, self.linked_list_2))
        self.assertEqual(union_1, fn_union_1)

        intersection_l = set_1.intersection(set_2)
        fn_intersection_1 = intersection(
            self.linked_list_1, self.linked_list_2)
        self.assertEqual(intersection_l, fn_intersection_1)

    def test_ui_2(self):
        set_3 = set(self.element_3)
        set_4 = set(self.element_4)
        union_2 = set_3.union(set_4)
        fn_union_2 = union(self.linked_list_3, self.linked_list_4)
        self.assertEqual(union_2, fn_union_2)

        intersection_2 = set_3.intersection(set_4)
        fn_intersection_2 = intersection(
            self.linked_list_3, self.linked_list_4)
        self.assertEqual(intersection_2, fn_intersection_2)

    def test_empty_ui(self):
        set_e1 = set()
        set_e2 = set()
        union_e = set_e1.union(set_e2)
        intersection_e = set_e1.intersection(set_e2)
        fn_union_e = union(self.linked_list_e1, self.linked_list_e2)
        fn_intersection_e = intersection(
            self.linked_list_e1, self.linked_list_e2)
        self.assertEqual(union_e, fn_union_e)
        self.assertEqual(intersection_e, fn_intersection_e)

    def test_null_empty_ui(self):
        set_n1 = set(self.nones)
        set_n2 = set(self.nones)

        union_n = set_n1.union(set_n2)
        intersection_n = set_n1.intersection(set_n2)

        fn_union_n = union(self.linked_list_n1, self.linked_list_n2)
        fn_intersection_n = intersection(
            self.linked_list_n1, self.linked_list_n2)

        self.assertEqual(union_n, fn_union_n)
        self.assertEqual(intersection_n, fn_intersection_n)


if __name__ == "__main__":
    unittest.main()
