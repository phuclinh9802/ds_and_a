# iterate with index
# keyword: enumerate
arr = [1,4,2]
for index, item in enumerate(arr):
    print(index, item)

# sort by 2nd letter
# keyword: lambda
arr_string = ['hi', 'hello']
print(sorted(arr_string, key=lambda k:k[1]))

# find the index of the first occurence of the item
print(arr.index(4))

# unpack and assign each item with n variables
a,b,c = arr
print(a,b,c)

# list comprehension
# create a loop inside a list
list_comp = [i*2 for i in range(10) if i > 2 and i < 7]
print(list_comp)

# delete an item or a list
del(list_comp[0])
print(list_comp)

# tuple initialization
tupl = (1,2,3)
# tupl = (); (1,2,3); 1,2,3; 1,


# tuple - member objects
# mutable
tupl = ([1,2,3], 3)
del(tupl[0][2])
print(tupl)

# tuple - concatenation
tupl += 4,
print(tupl)

# Sets
s = set()
s = set([1,3,5])
print(s)
# s = set(); {1,2,3,3} -> {1,2,3}; set([1,3,5])


# Dictionaries
diction = {'book':20, 'bag':30}
print(diction)
d = dict(book=20, bag=30)
print(d)
di = dict([('book', 20), ('bag', 30)])
print(di)