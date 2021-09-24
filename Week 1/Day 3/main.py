# MaxHeap: a complete binary tree data structure which has the condition: every node <= its parent
# Insert: O(logn)
# Get max: O(1)
# remove max: O(logn)
# access to specific node
# for instance: index = 4 -> parent(index) = i / 2, leftchild(index) = i * 2, rightchild(index) = i * 2 + 1
# Push (insert): push to the end or the tree (array), and float up to the proper position by comparing to its parent,
# if greater -> swap parent and pushing item, if not, done.
# pop (remove): swap the first and last index -> delete the element with last index -> bubble down the index 1 element
# -> if element at index 1 < left -> index 1 swap with index at left, and if element at index 1 < index at right child -> swap with right child
# -> bubble down recursively
# we have push, pop, peek, __bubbleDown, __floatUp

class MaxHeap():
    def __init__(self, items=[]): # original array
        super().__init__()
        self.heap = [0] # start from index 1
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    def push(self, item):
        self.heap.append(item) # add item into heap
        self.__floatUp(len(self.heap) - 1) # float up to proper position

    def pop(self):
        # swap index 1 to index at the end
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1) # swap between i = 1 & i = len(arr) - 1
            max = self.heap.pop() # store last element to be removed
            self.__bubbleDown(1)
        if len(self.heap) == 2:
            return self.heap.pop()
        if len(self.heap) < 2:
            return False

    def peek(self):
        if self.heap[1]: # if the first element in MaxHeap exists, return it
            return self.heap[1]
        return False

    def __swap(self, first, last):
        self.heap[first], self.heap[last] = self.heap[last] , self.heap[first]

    def __floatUp(self, index):
        # get parent of element at index
        parent = index // 2
        # base case
        if index <= 1:
            return
        # compare between el at index and its parent
        if self.heap[index] > self.heap[parent]:
            index = parent
            # swap them
            self.__swap(parent, index)
            self.__floatUp(parent) # float up to proper position again using recursion

    def __bubbleDown(self, index):
        # get left and right child index
        left = index * 2
        right = index * 2 + 1
        # store largest index
        largest = index

        # if left child > parent
        if left < len(self.heap) - 1 and self.heap[left] > self.heap[largest]:
            largest = left
        # if right child > parent
        if right < len(self.heap) - 1 and self.heap[right] > self.heap[largest]:
            largest = right
        # if largest index is changed, then swap them with original index, then do recursion
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)

# test MaxHeap code
heap = MaxHeap([5,2,4,1,555,323,13])
heap.push(9)
print(heap)

# LinkedList