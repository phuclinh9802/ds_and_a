# MaxHeap
# a data structure of complete binary tree - fast access to the elements in the list
# insert (O(log(n)))
# get max O(1)
# remove max O(log(n))
# functions: public: push, pop, peek, __str__
#            private: __swap__, __floatUp__, __bubbleDown__

# TODO: Implementation of MaxHeap()
class MaxHeap():
    # initialize MaxHeap with parameters:
    def __init__(self, items=[] ):
        super().__init__()
        self.heap=[0] # maxheap starts with index 1
        # put the items in the list in proper places
        for item in items:
            self.heap.append(item)
            # insert -> floatUp
            self.__floatUp__(len(self.heap) - 1)

    # --  PUBLIC  --
    # push
    def push(self, item):
        self.heap.append(item)
        self.__floatUp__(len(self.heap) - 1)

    # get max
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    # remove max:
    # swap 1 and len - 1 indexes
    # remove last index
    # bubble down the first index
    def pop(self):
        if len(self.heap) > 2:
            self.__swap__(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown__(1)
            return max
        if len(self.heap) == 2:
            return self.heap.pop()

        return False

    # -- PRIVATE --
    def __swap__(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp__(self, index):
        # get parent index
        parent = index // 2
        # comparison
        if self.heap[index] > self.heap[parent]:
            self.__swap__(index, parent)
            self.__floatUp__(parent)


    def __bubbleDown__(self, index):
        # get children's indices
        left = index * 2
        right = index * 2 + 1
        # store largest index
        largest = index
        # conditions
        # if left child > index
        if self.heap[left] < len(self.heap) - 1 and self.heap[left] > self.heap[largest]:
            largest = left
        # if right child > index
        if self.heap[right] < len(self.heap) - 1 and self.heap[right] > self.heap[largest]:
            largest = right

        # then we swap index with the updated largest index, if largest is changed
        if largest != index:
            self.__swap__(index, largest)
            # recursion
            self.__bubbleDown__(largest)

    # print string
    def __str__(self):
        return str(self.heap)



