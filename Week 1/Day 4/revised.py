# LinkedList
# a data structure that has elements in a list linked together by referencing
# e.g.: root -> (1,ref) -> (2, ref) -> None

# TODO: Create a Node class
# with param of data, ref to next node, ref to prev node
class Node():
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return "(" + str(self.data) + ")"

# TODO: Create a LinkedList class
# functions: add, find, remove, print
class LinkedList():
    def __init__(self, r=None ):
        self.root = r
        # size to keep track of size of the list
        self.size = 0

    # add
    def add(self, data):
        # start at root, initialize a new node with ref to the root
        new_node = Node(data, self.root)
        # set root node to new node to insert new node at the beginning
        self.root = new_node
        self.size += 1 # update size

    # get data
    def find(self, data):
        # start at root
        this_node = self.root
        while this_node is not None:
            # if found
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node

        return False
    # pop
    def remove(self, data):
        # start at root
        this_node = self.root
        # init prev node to keep track of prev node as well
        prev_node = None

        while this_node is not None:
            # if found
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else: # at root
                    self.root = this_node.next_node
                self.size -= 1
                return True # return if found
            else:
                prev_node = this_node
                this_node = this_node.next_node

        return False # not found

    # print list
    def print_list(self):
        # start at root
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print("None")

# test LinkedList
linked_list = LinkedList()
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
linked_list.add(6)

linked_list.print_list()
print(linked_list.find(3))
linked_list.remove(3)
linked_list.print_list()
