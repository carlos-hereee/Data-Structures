from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # push adds new items to the end of the array
    def push(self, value):
        self.storage.append(value)

    # pop remvoes items to the end of the array
    def pop(self):
        self.storage.pop()

    def len(self):
        len(self.storage)
