# key-value pairs from dictionaries
d = {'book': 20, 'bag': 30}

print(d.keys())
print(d.values())
print(d.items())

# check membership in key
if 'book' in d:
    print('exist!')
if 20 in d.values():
    print('value exists')

# iterate a dict in 2 ways
for k in d:
    print(k, d[k])

for k,v in d.items():
    print(k,v)

# list comprehension - more complex examples
# get numbers from a string
s = '1 l0v3 y0u'
l = [x for x in s if x.isnumeric()]
print(''.join(l))

# get index from an item in a list
name_list = ['Phillip', 'Nguyet']
l = [x for x, name in enumerate(name_list) if name == 'Phillip']
print(l)

# Stacks - LIFO DS
stack = list()
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop()

# Stack class (with push pop peek & print string
class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
# test Stack

st = Stack()
st.push(1)
st.push(2)
st.push(7)
print(st)
st.pop()
print(st)
print(st.peek())
print(st)

