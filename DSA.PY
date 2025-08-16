# Indexing: it always starts with zero.

# string
x = 'dog'
print(x[1])

# list
x = ['donkey', 'cow', 'zebra', 'pig']
print(x[1])

# tuple
x = ('Jack', 'Jael', 'Jacinta', 'Don')
print(x[0])

# Slicing = slice out substrings, sublists, subtuples, using indexes
# [start:end+:step] The start is always inclusive while the end is not inclusive
x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:2])
print(x[:5])
print(x[:3])

# adding/concatenating =combine two sequence of the same type
# string
x = 'goat' + 'pig'
print(x)
# list
y = ['dog', 'giraffe', 'monkey', 'elephant'] + ['lion', 'cub']
print(y)
# tuple
z = ('kelvin', 'Dorcas', 'June', 'Mary') + ('kata', 'liokp', 'Rast')
print(z)

# Checking membership=test whether an item is in the sequence or not
x = 'bug'
print('u' in x)
y = ['pig', 'donkey', 'goat', 'cow']
print('cow'not in y)
# number of items = cpunt the number of items in a sequence
y = ['pig', 'goat', 'donkey']
print(len(y))

# minimum= to find the minimum item in a sequence
y = ['pig', 'goat', 'donkey']
print(min(y))

# summation
z = [2, 6, 4, 9, 7]
print(sum(z))
print(sum[2:3])

# sorting = returns a new list of items in sorted order
x = 'bug'
print(sorted(x))
y = ['pig', 'dog', 'donkey', 'sheep']
print(sorted(y))

# count(item) = return count of an item
x = 'hippo'
print(x.count('p'))
y = ('craig', 'Ben', 'Betty')
print(y.count('Ben'))

# index
x = 'hippo'
print(x.index('p'))

x = [1, 3, 4, 5, 6, 7, 8]
del (x[3:2])
print(x)
del (x)  # delete the entire list.

x = [32, 32, 4, 6, 78, 89, 7, 6, 0]
x.append(43)  # add 43 to the list
print(x)

# Tuples(immutable, useful for fixed data,  faster than lists, sequence types) member ojects maybe mutable
x = ()
x = (1, 2, 3, 4)
x = 1, 2, 3, 4
x = 2,  # the comma tells python it is a tuple
print(x, type(x))
# member objects are mutable
x = 1, 2, 23, 3, 4, 5
# del(x[1])  #fails
print(x)

y = 1, 2, 3, 4
del (y[0])  # delete 1 the list within the tuple is mutable
print(y)

# Sets(store non duplicate items, faster access than lists, math set ops(union, intersect), sets are unordered)
x = {3, 5, 3, 5}
print(x)
y = set()
print(y)
list1 = [1, 2, 3, 4]
z = set(list1)
print(z)
# set operations
x = {3, 34.8, 9}
print(x)
x.add(7)
print(x)

x.remove(3)
print(x)

# get length of set
print(len(x))
# check membership of set x
print(3 in x)
# pop random item from set x
print(x.pop(), x)
# delete all items from the set x
x.clear()
print(x)

# Dictionaries(value pairs, are unordered)
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 33.9}
print(x)

x['shrimp'] = 38.8  # add or update
print(x)
del (x['shrimp'])
print(x)

# STACKS
