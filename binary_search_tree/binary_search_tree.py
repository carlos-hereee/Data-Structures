# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        # value would be the root
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less than root go left
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # else it will be greater and go right
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value is = to the target return true
        if target == self.value:
            return True
        # else if the target is greater than value go right and repeat
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        # else if the less is greater than value go right and repeat
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        # else the target is not in the tree
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # loop til i get to the furthest right
        if self.right is None:
            # when it is none that would be the max
            return self.value
        else:
            # else repeat
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

