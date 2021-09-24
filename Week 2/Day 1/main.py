# Doubly Linked List
# Node (prev node - data - next node)
# to delete node: we need to do both ways of a node to be deleted
# (prev, 1, next) -> (prev, 2, next) -> (prev, 3, next)
# -> add: (1): no node: self.root = new_node, self.last = self.root (last pointer points to the root since there is only 1 node)
# -> find: same as before
# -> delete: (1): middle node: this.prev.next = this.next.prev, this.next.prev = this.prev.next
#            (2): last node: this.prev.next = none, self.last = this.prev
#            (3): root node: self.root = this.next, this.next.prev = self.root
# Advantage:  - iterate in either direction
#             - can delete without iterating through the list
# have 2 node initially

# TODO: Create node class
class Node():
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return "(" + str(self.data) + ")"

# TODO: Create Doubly Linked List Class
class DoublyLinkedList():
    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def add(self, data):
        # 2 conditions:
        # (1): nothing in the list
        if self.size == 0:
            self.root = Node(data) # create a new node and points root to new node
            self.last = self.root # also points last pointer to the new node, since there is only one node in the list
        else: # if there is more than one node
            new_node = Node(data, self.root) # new_node.next_node = self.root -> push the root node to next
            self.root.prev_node = new_node # point the old root node's prev node ref to new node for doubly linked list
            self.root = new_node # point root pointer to new node

        self.size += 1

    def find(self, data):
        # 2 conditions inside the while loop
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            elif this_node.next_node is None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, data):
        # keep track
        this_node = self.root

        while this_node is not None:
            # 2 main conditions - found / not found
            if this_node.data == data:
                # 3 subconditions - middle node / root node / last node
                if this_node.prev_node is not None:
                    if this_node.next_node is not None: # middle node
                        this_node.prev_node.next_node = this_node.next_node.prev_node
                        this_node.next_node.prev_node = this_node.prev_node.next_node
                    else: # last node
                        this_node.prev_node = None # prev node points to none
                        self.last = this_node.prev_node # new last node
                else: # root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
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

