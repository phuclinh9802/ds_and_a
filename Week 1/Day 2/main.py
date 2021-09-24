# key-value pairs from dictionaries
kv = {'beef': 30, 'pork': 20}

# print key
print(kv.keys())
print(kv.values())
print(kv.items()) # print out key-value tuples.

# check membership in key
if 'beef' in kv:
    print('True that')
if 30 in kv.values():
    print("True")

# iterate a dict in 2 ways
#1:
for key in kv:
    print(key, kv[key]) # dict[key] = value associated with key
#2:
for key, value in kv.items():
    print(key,value)

# list comprehension - more complex examples
# get numbers from a string
s = 'I l0v3 Nguyet 9 tim35'
nums = [x for x in s if x.isnumeric()]
print(''.join(nums)) # join all numbers inside the list nums
# get index from an item in a list
alist = ['Phil', 'Nguyet', 'Austin']
ind_list = [k for k,v in enumerate(alist) if v == 'Nguyet']
print(ind_list)

# Stacks - LIFO DS
# push - pop operations
# push: add an item on top of the stack
# pop: return the item on top and remove it
# peek: return the item on top without removing it
# clear: clear the stack
# Application: undo
# Implementation:
lifo = list()

# push
lifo.append(2)
lifo.append(3)
print(lifo)

# pop
print(lifo.pop())

# since peek & print out string does not have on the list function for stack, we can create a wrapper class w/ constructors & methods.

class Stack():
    def __init__(self):
        self.stack = list()
    # push
    def push(self, item):
        return self.stack.append(item)
    # pop
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    # peek
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    # print out string
    def __str__(self):
        return str(self.stack)

# test Stack code
my_stack = Stack()
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack)

# Queue using deque from collections
from collections import deque

queue = deque()
queue.append(5)
queue.append(10)
print(queue)
print(queue.popleft())
print(queue)

# TODO: Create a Queue wrapper class
# enqueue - dequeue - peek - print
class Queue():
    def __init__(self):
        self.queue = list()
    def enqueue(self, item):
        if len(self.queue) > 0:
            return self.queue.insert(0,item)
        else:
            return self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[len(self.queue) - 1]
        else:
            return None
    def __str__(self):
        return str(self.queue)

# TODO: Test Queue class
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q)
print(q.dequeue())
print(q)









