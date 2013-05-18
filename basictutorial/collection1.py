# chapter 1 - chapter 4

# find a prime number
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'


# even or odd 
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
 
    
# fibonacci number
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
        
# default argument values
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

#  Default Arguments attention
"""
Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
"""
def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)
"""
This will print
[1]
[1, 2]
[1, 2, 3]
"""

## 4.7.2 Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
# !!!
# if do not assign a valut to voltage, there will be an error.
# parrot(state='1000')
                                  
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
"""
All the keyword arguments passed must match one of the arguments accepted by the function, and their order is not important. 
This also includes non-optional arguments is valid too). 
No argument may receive a value more than once. 
"""
# **name receives a dictionary
# *name receives a tuple
# !!!!! *name must occur before **name.
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    
    for arg in arguments:
        print arg
        
    print "-" * 40
    
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
# Two sentences after the first arg are treated as one tuple, and be accepted by *arguments
# shopkeeper = ... client = ... are treated as an anonymous dictionary 
#     with keys of shopkeeper, client and sketch
"""
Some Reference
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
"""

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

'''
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch
'''
#===============================================================================
# 
# >>> range(3, 6)             # normal call with separate arguments
# [3, 4, 5]
# >>> args = [3, 6]
# >>> range(*args)            # call with arguments unpacked from a list
# [3, 4, 5]
#====================================
'''Unpack Arguments'''
# >>> def parrot(voltage, state='a stiff', action='voom'):
# ...     print "-- This parrot wouldn't", action,
# ...     print "if you put", voltage, "volts through it.",
# ...     print "E's", state, "!"
# ...
# >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# >>> parrot(**d)
# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
#
#===============================================================================


#!!! Lamda forms
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print f(0) #42

print f(1) #43

print f(0) #42


# 4.7.6 Documentation String
'''
The first line should always be a short, concise summary of the object's purpose.
The second line should be blank, visually separating the summary from the rest of the description
The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.
'''

def my_function():
    """
    Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print my_function.__doc__
#     Do nothing, but document it.
#     
#     No, really, it doesn't do anything.


'''
Here are the most important points extracted for you:

1.Use 4-space indentation, and no tabs.
2.Use blank lines to separate functions and classes, and larger blocks of code inside functions.
3.When possible, put comments on a line of their own.
4.Use docstrings.
5.Name your classes with CamelCase 
6.Name your functions with lower_case_with_underscores 
7.Always use self as the name for the first method argument.
'''

# End of chapter 4
