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
Important warning: The default value is evaluated only once. 
This makes a difference when the default is a mutable object 
    such as a list, dictionary, or instances of most classes.
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

