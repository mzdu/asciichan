# Classes

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    
    # this is the initialize method, which runs automatically when a new object has been created.
    def __init__(self):
        print 'hello init1'


class MyClass2(MyClass):
    
    def k(self):
        return 'h'
    
    def k2(self):
        print MyClass.f(self)  
    
x = MyClass()
print x.i           #12345
print x.f()         #hello world

# Must use inheritance, otherwise, there will be an error.
y = MyClass2()
y.k2()
#===============================================================================
# Output
# 
# hello init1
# 12345
# hello world
# hello init1
# hello world
#===============================================================================


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print x.i, x.r    #-4.5  3.0

# ??!!!
x.counter = 1
# this works. and counter has been added to the object x
print x.counter


# !!!!!
# delete counter attribute from the object x
del x.counter
# print x.counter generates an error.
# print x.counter



"""
 It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. 
"""


# Function defined outside the class
def f1(x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
    def __init__(self):
        print f1(100,300)
    
d = C()    
del d
    
print "===================================="

# An Example
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
    
# Inheritance
'''
1. Use isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

2. Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(unicode, str) is False since unicode is not a subclass of str (they only share a common ancestor, basestring).
'''

# Private Attribute
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # once you name your varible like __xx(), it will be a private type automatically.
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
            


# Abstract

class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000    
    
# 9.9 Iterators
for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for sth in {'one':1, 'two':2}:
    print 'it is the key', sth
for char in "123":
    print char
for line in open("./static/myfile.txt"):
    print line
    
    # Befind the scenes
'''
the for statement calls iter() on the container object. The function returns an iterator object that defines the method next() which accesses elements in the container one at a time. When there are no more elements, next() raises a StopIteration exception which tells the for loop to terminate. 
'''
s = 'abc'
it = iter(s)
print it

print it.next()  #a

print it.next()  #b

print it.next()  #c

try:
    print it.next()  # this iteration reaches the end of string, and raises an exception StopIteration
except:
    print 'woops'


# 1. how to use generator
# 2. what is a yield
# Pay extra attention on this.