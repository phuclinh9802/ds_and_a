# Trees
# e.g: Modeling organization
# Binary Tree: each parent has up to 2 child node
# ancestors, descendants.
# Binary Search Tree: node > left subtree, node > right subtree
# Operations: Insert, find, delete, get_size, traversals (mostly recursion)
# Insert: Start at root, always insert as a leaf
#       - if node < subtree -> go to the left, and node > subtree -> go to the right
#       - if at leaf -> insert correct position
# Find: Start at root, same as insert op. return the data if found
# Delete: 3 possible conditions: leaf, parent, 2 children
# (1): leaf: delete it...
# (2): node with 1 child node: promote the child to the target node's position, and its child's children
# (3): node with 2 children: find the next highest node after the node to be deleted, and children comes with that node to be promoted
# Get_size: returns # of nodes, works recursively: size = 1 + size(left_subtree) + size(right_subtree)
# Traversals:
# (1): pre-order: visit root before subtrees (NLR)
# (2): in-order: visit the root between subtrees (LNR)
# Speed: fast
# Insert, Delete, Find: O(logn)

# Implementation
class Tree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Insert
    def insert(self, data):
        # 3 conditions
        # duplicative value -> False
        if self.data == data:
            return False
        # left tree
        elif self.data > data:
            # check if left child is none
            if self.left is not None:
                # recursively continue through left children
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        # right tree
        if self.data < data:
            # check if right child is none
            if self.right is not None:
                # recursively continue through right child
                self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    # find - same as insert
    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data: # data is less than the current node's data
            if self.left is not None:
                return self.left.find(data)
            else:
                return False
        else: # data is greater than the current node's data
            if self.right is not None:
                return self.right.find(data)
            else:
                return False

    # delete
    def delete(self, data): # more info, go to https://techiedelight.com/deletion-from-bst/
        # initialize parent to keep track of self's parent
        parent = None
        # start from root
        current = self

        # set the parent of the node to be deleted's pointer
        while current is not None and current.data != data:
            # set parent pointer
            parent = current

            # check the value of the data > or < current node's data
            if current.data < data:
                current = current.right
            elif current.data > data:
                current = current.left

        # if the data is not found
        if current is None:
            return False
