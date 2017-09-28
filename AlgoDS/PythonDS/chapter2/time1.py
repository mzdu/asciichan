# This is the demo of using time
import time

# algorithm1 to calculate the sum of N
def sumOfN(n):
    start = time.time()
    theSum = 0
    # O(n)
    for i in range(1,n+1):
        theSum = theSum + i
    
    end = time.time()
#    print 'time,end,start',end,start
    return theSum,end-start

# Algorithm with constant time complexity, to calculate the sum of N

# O(1)
def sumOfN3(n):
    start = time.time()
    theSum = (n*(n+1))/2
    end = time.time()
    
    return theSum,end-start


for i in range(20):
    print "Sum is %d required %10.7f seconds" %sumOfN(100000)

print "-----------------------------------------------"

for i in range(20):
    print "Sum is %d required %10.7f seconds" %sumOfN3(100000)

# from the time, we could clearly compare the difference of O(n) and O(1)