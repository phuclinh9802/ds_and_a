# Doubly Linked List
# same as regular linked list, the difference is that the node has both ref to next and prev node
# have functions: add, find, remove, print_list
# initalization: root and last node, size
# add: 2 conditions: when there is no elements in the list, and there is one or more node in the list
# find: same as before
# remove: run thorugh while loop per usual.
#       2 main conditions:
#       -   data found
#       -   data not found
#       3 sub conditions for data found:
#       -   node in the middle
#       -   node at last pos
#       -   node at root
#       when data is not found:
#       -   move to next node of this node
#       Finally, return false if not found anything
# print_list: starting from printing the root node, then go through the while loop

# TODO: create a node class
class Node():
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return "(" + str(self.data) + ")"


# TODO: create a doubly linked list class
class DoublyLinkedList():
    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data) # point root directly to the new node
            self.last = self.root # point last to root node
        else:
            new_node = Node(data, self.root) # new_node.next_node = self.root
            self.root.prev_node = new_node.next_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root

        while this_node is not None:
            if this_node.data == data:
                return data
            elif this_node.next_node is None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root

        while this_node is not None:
            if this_node.data == data:
                # with prev node
                if this_node.prev_node is not None:
                    # mid node
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node.prev_node
                        this_node.next_node.prev_node = this_node.prev_node.next_node
                    # last node
                    else:
                        this_node.prev_node = None
                        self.last = this_node.prev_node

                    self.size -= 1
                # without prev node - root
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
            # no node found
            else:
                this_node = this_node.next_node
        return False

    def print_list(self):
        # base case
        if self.root is None:
            return

        this_node = self.root
        print(this_node, end="->")
        while this_node is not None:
            this_node = this_node.next_node
            print(this_node, end="->")

# TODO: test code
doublyll = DoublyLinkedList()
doublyll.add(2)
doublyll.add(3)
doublyll.add(4)
doublyll.print_list()
