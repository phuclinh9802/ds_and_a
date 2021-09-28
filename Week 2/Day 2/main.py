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

    # delete - need function to support
    # getMinNode
    def getMinNode(self, node):
        while node.left:
            node = node.left

        return node

    # delete implementation
    def delete(self, data): # more info, go to https://techiedelight.com/deletion-from-bst/
        # initialize parent to keep track of self's parent
        parent = None
        # start from root
        current = self
        # root node
        root = self

        # set the parent of the node to be deleted's pointer
        while current is not None and current.data != data:
            # set parent pointer
            parent = current
            # root node
            root = self

            # check the value of the data > or < current node's data
            if current.data < data:
                current = current.right
            elif current.data > data:
                current = current.left

        # if the data is not found
        if current is None:
            return False

        # Case 1: Leaf Node
        if current.left is None and current.right is None:
            # if leaf node is not root node
            if current != root:
                # check if parent's left node = current node
                if parent.left == current:
                    parent.left = None
                elif parent.right == current:
                    parent.right = None

            # if leaf node is root node
                root = None

        # Case 2: Node to be deleted has 2 children
        if current.left and current.right:
            # get the next min node to replace the current node
            # need a supported function to get leftmost node of the right child
            min_node = self.getMinNode(current.right)

            # store the successor value
            val = min_node.data

            # recursively call
            self.delete(min_node.data)

            # copy val of successor to current node
            current.data = val

        # Note:
        # example: delete(20)
        # parent = 15, current=20 -> case 2
        # min_node = 30
        # val = 30
        # recursive: delete(30)
        # -> case 1: leaf node -> parent = 20, current = 30 -> parent.right = None -> return self
        # -> current.data = 30 => We are done!
        # 2nd choice, we can also get max of left child

        # Case 3: Node to be deleted has 1 child
        if current.left or current.right:
            if current.left:
                # store child node
                child = current.left
            elif current.right:
                # store child node
                child = current.right

            # if not root
            if current != root:
                if parent.left == current:
                    parent.left = child # skip deleted node
                elif parent.right == current:
                    parent.right = child # skip deleted node

            # if root
            if current == root:
                root = child

    # get_size
    def get_size(self):
        # recursion
        if self.left and self.right:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()

    # preorder (NLR)
    def preorder(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    # inorder
    def inorder(self):
        # check if current root is not none
        if self is not None:
            # go through the left first
            if self.left:
                self.left.inorder()
            # get root in between
            print(self.data, end=" ")
            # go through right subtree
            if self.right:
                self.right.inorder()

# test BST code
bst = Tree(7)

bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(8)
bst.insert(9)
print(bst.find(3))
bst.preorder()
