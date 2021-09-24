# Circular LinkedList
# same as regular linked list, difference is that the ref to next node of last node is the root
# e.g.: root -> (1,ref) -> (2, ref) -> root
# add: 2 conditions - first: if there is no node -> add node and make root point to the new node
#                   - second: if there is more than one node -> add node and make root.next_node point to the new node
# find: if data is found -> return the data. If not, contiinue through while loop and move to next node. If the next node is root, then return false
# remove: a. if the data is found: 2 conditions
# - 1st: prev node is not none -> we can point prev_node.next_node to this_node.next_node to
# skip this_node.
# - 2nd: prev node is none -> delete root node -> go through while loop & through the list until there is a node pointing back to root node.
#       -> set this_node.next_node instead pointing to self.root, it points to root's next node, and set the new root to the root's next node
#       -> update size & return True to finish the function
#         b. if the data is not found yet:
#         if prev_node is none -> set prev_node = self.root, and this_node to next node
#         else -> prev_node = this_node, this_node = this_node.next_node
#         c. if the data is not found (points back to root node and cannot find the data)
#          return False


# TODO: Node class
class Node():
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return "(" +  str(self.data) + ")"

# Todo: Implementation
class CircularLinkedList():
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    # add
    def add(self, data):
        # if there is no node -> create new node and points to itself
        if self.size == 0:
            # initialize new node
            new_node = Node(data)
            self.root = new_node
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node) # new_node.next_node = self.root.next_node
            self.root.next_node = new_node
        # increase size
        self.size += 1

    # find
    def find(self, data):
        # store node to keep track of the list from the start
        this_node = self.root

        while True:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.root:
                return False
            else:
                this_node = this_node.next_node

    # remove
    def remove(self, data):
        # store node & start from root
        this_node = self.root
        # keep track of prev node
        prev_node = None

        while True:
            # if data is found
            if this_node.data == data:
                # if prev node exists
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                # if prev node does not exist (delete the root)
                else:
                    while this_node.next_node != self.root: # go through the list until the last node
                        this_node = this_node.next_node
                    self.root = this_node.next_node
                    self.root.next_node = self.root
                self.size -= 1
                return True

            # if data is not found
            # if points to root again
            elif this_node.next_node == self.root:
                return False
            else:
                prev_node = this_node
                this_node = this_node.next_node

    # print_list: print root node first, then go through the list
    def print_list(self):
        # if the list does not exist the root node -> return
        if self.size == 0:
            return

        this_node = self.root
        print(this_node, end="->")

        # while the node's next node does not point to the root again
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end="->")
        print(self.root)

# TODO: test CircularLinkedList implementation
circular = CircularLinkedList()
circular.add(1)
circular.add(2)
circular.add(3)
circular.add(5)
circular.add(6)
circular.print_list()
print(circular.find(4))
circular.remove(3)
circular.print_list()
