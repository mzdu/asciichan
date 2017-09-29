# 5.1 Lists

#===============================================================================
# 
# list.append(x)
# Add an item to the end of the list; equivalent to a[len(a):] = [x].
# 
# list.extend(L)
# Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
# 
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# 
# list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item.
# 
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. 
# (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
# 
# list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.
# 
# list.count(x)
# Return the number of times x appears in the list.
# 
# list.sort()
# Sort the items of the list, in place.
# 
# list.reverse()
# Reverse the elements of the list, in place.
#===============================================================================

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
#2 1 0
a.insert(2, -1)
a.append(333)
a
#[66.25, 333, -1, 333, 1, 1234.5, 333]
a.index(333)
#1
a.remove(333)
a
#[66.25, -1, 333, 1, 1234.5, 333]
a.reverse()
a
#[333, 1234.5, 1, 333, -1, 66.25]
a.sort()
a
#[-1, 1, 66.25, 333, 333, 1234.5]

"""
5.1.1 Using Lists as Stacks

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
"""


"""
5.1.2 Using Lists as Queues

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
"""
# Here I use pop(0) to implement the idea of queue

queue = ["Eric", "John", "Michael"]
queue.append("Bob")
print queue.pop(0)   # Eric
print queue          # ['John', 'Michael', 'Bob']



"""
5.1.3 Functional Programming Tools
filter(), map(), and reduce().

filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true.
map(function, sequence) calls function(item) for each of the sequence's items and returns a list of the return values. 
reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence,
                           then on the result and the next item, and so on.

"""
def f(x): return x % 2 != 0 and x % 3 != 0
# filter gets the value of x instead of return value
filter(f, range(2, 25))          #[5, 7, 11, 13, 17, 19, 23]


def cube(x): return x*x*x
# map gets the return value 
map(cube, range(1, 11))          #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

seq = range(8)
def add(x, y): return x+y
# x y get numbers from seq list seperately
map(add, seq, seq)               #[0, 2, 4, 6, 8, 10, 12, 14]

def add2(x,y,z): return x+y+z
# reduce returns the sum of numbers from 1 to 10
# for this example, you can use as many parameters as you want
# because all the numbers will be added together
print reduce(add, range(1, 11))        # 55

"""
5.1.4 List Comprehension  !!! Very Interesting
"""
squares = [x**2 for x in range(10)]  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

list2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]  
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

"""
# More Advanced Discussions

>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# zip() 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print zip(*matrix)  
#[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]



# 5.3 Tuples and Sequences
#===============================================================================
# >>> empty = ()
# >>> singleton = 'hello',    # <-- note trailing comma
# >>> len(empty)
# 0
# >>> len(singleton)
# 1
# >>> singleton
# ('hello',)
#===============================================================================


# 5.4 Sets
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
fruit
set(['orange', 'pear', 'apple', 'banana'])
'orange' in fruit                 # fast membership testing
True
'crabgrass' in fruit
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
a & b                              # letters in both a and b
set(['a', 'c'])
a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])

# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'} # find letters not in that string
a                                  # set(['r', 'd'])

# 5.5 Dictionaries
"""
1. You can't use lists as keys, since lists can be modified in place using index assignments, 
   slice assignments, or methods like append() and extend().
2. The keys() method of a dictionary object returns a list of all the keys used in the dictionary, 
   in arbitrary order (if you want it sorted, just apply the sorted() function to it). 
3. To check whether a single key is in the dictionary, use the in keyword.
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 412
print tel                 # {'sape': 4139, 'guido': 4127, 'jack': 4098}
print tel['jack']         # 4098
del tel['sape']
tel['irv'] = 4127
print tel                 # {'guido': 4127, 'irv': 4127, 'jack': 4098}
print tel.keys()          # ['guido', 'irv', 'jack']
print 'guido' in tel      # True

# Two ways to create a dictionary
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'jack': 4098, 'guido': 4127}
print dict(sape=4139, guido=4127, jack=4098)  
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

print {x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}


# 5.6 Looping Techniques
"""
!!! enumerate()
"""
for i, v in enumerate(['tic','tac','toe']):
    print i, v
    
"""
0 tic
1 tac
2 toe
"""

# zip()
list1 = ['tic','tac','toe']
color = ['Red','Green','Blue']
others = ['air','dust']
print zip(list1,color)    
#[('tic', 'Red'), ('tac', 'Green'), ('toe', 'Blue')]
print zip(list1,color,others)
#[('tic', 'Red', 'air'), ('tac', 'Green', 'dust')]


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    # Pay more attention on this!!!!!!!
    print 'What is your {0}?  It is {1}.'.format(q, a)
    print 'Second try, print %s?  It is %s.' % (q, a)
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

for i in reversed(range(1,10,2)):
    print i

# set(), one of the most important usage: to eliminate the duplicates
# !!!!!!!!!!!!!!!!!!!!    
print set('hello world')

# iteritems() retrieve key and value at the same time
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v
    
# !!!
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print non_null                #Trondheim  
# Trondheim is the first Non-false value, and those three strings are connected by or
# so the assignment catches the first non-error value -- Trondheim


# 5.8 Comparing Sequences and Other Types
'''
!!!
The comparison uses lexicographical ordering: first the first two items are compared, 
and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, 
until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, 
the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. 
If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. 
Lexicographical ordering for strings uses the ASCII ordering for individual characters. 
!!!
'''
#===============================================================================
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
#===============================================================================

# end of chapter 5