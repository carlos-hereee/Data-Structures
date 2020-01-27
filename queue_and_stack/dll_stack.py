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
        return self.storage.add_to_tail(value)

    # pop remvoes items to the end of the array
    def pop(self):
        # what if no items on stack
        if self.storage.__len__() == 0:
            return
        else:
            return self.storage.remove_from_tail()

    # length of list
    def len(self):
        return self.storage.__len__()
