# LinkedList
# a data structure with element in a list linked together
# root -> (2, ref) -> (3, ref) -> (4, none)
# create Node class and LinkedList class

class Node():
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


# LinkedList class
# functions: add, find, remove, print
# add: start at root, assign new node with params with data & ref to root node -> root node is 2nd node
#       -> then, assign root node to new node (no need to assign new node's next node since root node already has it
# find: start from root node, find the node through while loop -> if node not none -> 2 possibilities
#       if data is found -> return data
#       else then move on to next node by assigning this node to ref to next node
# remove: we need 2 nodes, prev and next; start from root node, run through while loop (thisnode not none)
#         if data is found -> possibilities:
#         if prev is valid -> prev.nextnode = thisnode.nextnode , so thisnode does not exist in the linkedlist
#         if not, assign root node to the thisnode.nextnode
#         if data is not found yet -> prev = thisnode, thisnode = thisnode.nextnode
# print_list: basically run through a while loop again, and print

class LinkedList():
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)

        self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return False

    def remove(self, data):
        this_node = self.root
        # since prev node is nothing yet
        prev_node = None
        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:  # the node is in the root
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False


    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print(None)


# test LinkedList
linked_list = LinkedList()
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
linked_list.print_list()
linked_list.remove(5)
linked_list.print_list()