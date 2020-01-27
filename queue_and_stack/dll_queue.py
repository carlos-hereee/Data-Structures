from doubly_linked_list import DoublyLinkedList
import sys


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # should add an itemt o the back of the queue
    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    # should remove and return an item from the front of the queue
    def dequeue(self):
        # what if the queue is empty
        if self.storage.__len__() == 0:
            return
        # else remove it from the front
        else:
            return self.storage.remove_from_head()

    # returns the numver of items int he queue
    def len(self):
        # using the len method
        return self.storage.__len__()
