# TODO: iterate with index
x = [1,2,3]
for i, el in enumerate(x):
    print(i, el)


# TODO: sort by 2nd letter
letters = ['Hi', 'Hello']
print(sorted(letters, key=lambda k:k[1]))

# TODO: find the index of first occurrence of an item
string = 'fnsefmnlsfnm'
print(string.index('e'))

# TODO: unpack and assign each item in an array to n variables
a,b = letters
print(a,b)

# TODO: list comprehension - create a for loop inside a list
nums = [x**2 for x in range(5) if x > 2]
print(nums)

# TODO: delete an item or a list
del(letters[0])
print(letters)


# TODO: tuple
tupl = (1, 2, 3)
# tupl = 1, 2, 3
# tupl = 1,

# TODO: tuples are immutable, but its member objects are mutable
tup = ([1,2], 3)
del(tup[0][0])
print(tup)

# TODO: concatenate with tuples
tup += 4,
print(tup)

# TODO: Sets:
sets = {1,2,3}
# sets = set([1,2,3])
# non-duplicate

# TODO: Dictionaries
dic = {'book': 20, 'bag': 30}
print(dic)
dic = dict(book=20, bag=30)
print(dic)


# TODO: key-value pairs from dictionaries

# TODO: print key
print(dic.keys())
print(dic.values())
print(dic.items())

# TODO: check membership in key
if 'book' in dic:
    print(True)
if 20 in dic.values():
    print(True)

# TODO: iterate a dict in 2 ways
# 1
for x in dic:
    print(x, dic[x])
# 2
for x, y in dic.items():
    print(x, y)

# list comprehension - more complex examples
# TODO: get numbers from a string
string = '1 l0v3 y0u'
str_list = [x for x in string if x.isnumeric()]
print(''.join(str_list))

# TODO: get index from an item in a list
names = ['Phillip', "Nguyet"]
index_list = [x for x, name in enumerate(names) if name == 'Phillip']
print(index_list)

# TODO: Stacks - LIFO DS
# push - pop
stacks = list()
stacks.append(2)
stacks.append(3)
stacks.append(4)
print(stacks)
print(stacks.pop())
print(stacks)

# TODO: since peek & print out string does not have on the list function for stack, we can create a wrapper class w/ constructors & methods.
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]

    def __str__(self):
        return str(self.stack)

# TODO: test Stack code
st = Stack()
st.push(3)
st.push(5)
st.push(6)
print(st)
print(st.pop())
print(st)
print(st.peek())
print(st)

# TODO: Queue using deque from collections
from _collections import deque
que = deque()
que.append(3)
que.append(4)
print(que)
print(que.popleft())
print(que)


# TODO: Create a Queue wrapper class
# enqueue - dequeue - peek - print
class Queue():
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        if len(self.queue) > 0:
            return self.queue.insert(0, data)
        else:
            return self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 1:
            return self.queue.pop()
        return None

    def peek(self):
        if len(self.queue) > 1:
            return self.queue[len(self.queue) - 1]
        return None

    def __str__(self):
        return str(self.queue)


# TODO: Test Queue class
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)

# TODO: MaxHeap:
# maxheap : a complete binary tree with parent > its child
# we have: public functions: add, remove max, get max
#          private functions: __floatUp, __bubbleDown, __swap
# add: add to the list by appending, and floatUp: compare between the new element and its parent
#      if new el > parent -> index at new el = index at parent
#       so we can swap and continue by recursion -> if new el < parent -> return
# get max: return heap[1] (since the heap starts at index 1)
# remove max: __bubbleDown method:
#  step 1: swap heap[1] and heap[len(heap) - 1]
#  step 2: pop() to remove max in heap
#  step 3: bubbleDown the first element in heap
#           - test if heap at index 1's children > heap[1]. If so, set index at largest to left child's index or right child's index.
#           - we can swap the largest index to the first index and do this recursively.
class MaxHeap():
    def __init__(self, items=[]):
        self.heap = [0]
        for x in items:
            self.heap.append(x)
            self.__floatUp(len(self.heap) - 1)

    def add(self, data):
            self.heap.append(data)
            self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            return None

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        # base case
        if index <= 1:
            return
        if self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if left < len(self.heap) - 1 and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) - 1 and self.heap[right] > self.heap[largest]:
            largest = right

        if index != largest:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)

# TODO: test MaxHeap code
max_heap = MaxHeap([3,4,5])
max_heap.add(6)
print(max_heap)

# TODO: Node
class Node():
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return "(" + str(self.data) + ")"


# TODO: LinkedList
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
        prev_node = None

        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
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

        print("None")

# TODO: test LinkedList
linked_list = LinkedList()
linked_list.add(3)
linked_list.add(6)
linked_list.add(9)
linked_list.print_list()





# TODO: Circular LinkedList
class CircularLinkedList():
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, data):
        if self.size == 0:
            new_node = Node(data)
            self.root = new_node
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node) #new_node.next_node = self.root.next_node
            self.root.next_node = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root

        while True:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.root:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    self.root = this_node.next_node
                    self.root.next_node = self.root
                self.size -= 1
                return True

            elif this_node.next_node == self.root:
                return False
            else:
                prev_node = this_node
                this_node = this_node.next_node

    def print_list(self):
        this_node = self.root

        while True:
            print(this_node, end="->")
            this_node = this_node.next_node
            if this_node == self.root:
                return

circular = CircularLinkedList()
circular.add(1)
circular.add(2)
circular.add(3)
circular.print_list()