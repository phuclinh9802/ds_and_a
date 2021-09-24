# python Data Structures & Algorithm study

# iterate with index

y = [3,5,6]
for index, item in enumerate(y):
    print(index, item)

# sort by 2nd letter
x = ['hello', 'hi', 'xin chao', 'gc']

print(sorted(x, key=lambda k : k[1]))

# find the index of first occurence of an item
letter = 'djeqnakocie'

print(letter.index('q'))

# unpack and assign each item in an array to n variables
arr = [2,34,6]

a,b,c = arr
print(a,b,c)

# list comprehension - create a for loop inside a list
loop_list = [i**2 for i in range(5)]
print(loop_list)

# delete an item or a list
a_list = [3,5,6,1]
del(a_list[1])
print(a_list)
# del(a_list) -> a_list does not exist anymore

# append, extend, pop, remove, reverse, sort

# tuple
# several ways to initialize tuple:
# x = (), x = (1,2,3), x = 1,2,3 , x = 1,
x = 1,2,3
print(x)

# tuples are immutable, but its member objects are mutable
x = ([1,3], 4)
del(x[0][1])
print(x)
# concatenate with tuples
x += (6,)
print(x)

# Sets:
# Non-duplicate
# Very fast access vs. List
# Can be used for math sets (union, intersect)
# Unordered (cannot sort)
x = set() # empty set
x = {6,3,3}
print(x)
# functions: add(), remove(), clear(), pop() - pop a random item

# Dictionaries
# Ways to initialize
x = {'pork': 20, 'beef': 23, 'chicken': 30}
y = dict([('pork', 20), ('beef', 23), ('chicken', 30)]) # list of tuples passed through dictionaries function
z = dict(pork=20, beef=23, chicken=30)

print(x)
print(y)
print(z)

