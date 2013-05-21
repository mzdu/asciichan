# Starts from Chapter 6 Modules


def tempfunc():
    # fib and fib2 can only be ran inside of tempfunc()
    from fibo import fib, fib2
    fib(1000)
    print fib2(1000)
    
    # import fibo
    # fibo.fib(1000)
    
    print 'hello'

tempfunc()

#===============================================================================
# When you run a Python module with
# python fibo.py <arguments>
# the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
# you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the "main" file:
# $ python fibo.py 50
# 1 1 2 3 5 8 13 21 34
# If the module is imported, the code is not run:
# >>>
# import fibo
# 
# This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).
#===============================================================================

'''
import sys
def tempfunc2():
    
    sys.path.append('E:\\workspace\\asciichan\\basictutorial\\testpack')
    #from fibo import fib1
    print '======================='
    #fib(100)
    
#tempfunc2()

if sys.path[-1] == 'E:\workspace\asciichan\basictutorial\testpack':
    sys.path.pop()
    
print sys.path
'''

# Chapter 7 Input and Output

# write() 

"""
Two ways to create any format string
1. Use %s  %  v1
2. Use the str.format() method.
"""

# str() VS repr()
"""
str() is more human readable. It returns the final string we can see.
repr() returns the raw string.
"""
a = 'string111'
print repr(a)

    # another example
s = 'Hello, world.'
print str(s)   # Hello, World.

print repr(s)  # 'Hello, world.'

str(1.0/7.0)

repr(1.0/7.0)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print hellos

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

print '=========='
print repr(212.111) + repr(012.11212121)   #212.11112.11212121

"""
str.rjust() method of string objects, which right-justifies a string in a field of a given width 
                    by padding it with spaces on the left. 
There are similar methods str.ljust() and str.center()
"""


print '{0} and {1}'.format('spam', 'eggs')   # spam and eggs

print '{1} and {0}'.format('spam', 'eggs')   # eggs and spam

# 7.1.1 Traditional string formatting
import math
print 'The value of PI is approximately %5.3f.' % math.pi  #3.142

# 7.2 Reading and Writing Files
'''
open() returns a file object.
'''

# f = open('./testpack/test2.txt','r+')   
# print f   #<open file './testpack/test2.txt', mode 'r+' at 0x02510CD8>

'''
Some references of second argument
w : only writing, existing file with the same name will be erased.
r : read only
a : append to the end of file
r+ : open files for both reading and writing
b : appends to the mode opens the file in binary mode.
rb, wb, r+b look up above explanations
'''

# read() VS readline()
# read() fetch the entire file.
# readline() only throw out one line of file.

# print f.read()   
# print f.readline()
# print f.readline()
# print f.readline()

# compare the differences between read() and for line in f 
# for line in f:
#     print line


# this sentence will be written on the first line of file.
# You need to use for line in f: to control the location of cursor

# f.write('this is an additional line \n')

a = [0,1,2,3]

for i in a:
    open('/test2.txt','a').write(str(i))

#add test
