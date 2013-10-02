
from timeit import Timer


index1 = Timer("x[-1]",
                "from __main__ import x")
index2 = Timer("x[len(x)-1]",
               "from __main__ import x")
pop1 = Timer("x.pop(0)",
                "from __main__ import x")


print("index1   index2   pop(0)")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    in1 = index1.timeit(number=1000)
    x = list(range(i))
    in2 = index2.timeit(number=1000)
    x = list(range(i))
    p1 = pop1.timeit(number=1000)
    
    print("%15.5f, %15.5f, %15.5f" %(in1,in2,p1))
    
    
"""
        0.00018,         0.00033,         1.90102
        0.00014,         0.00033,         3.76953
        0.00229,         0.00033,         5.67419
        0.00014,         0.00035,         7.56062
        0.00014,         0.00033,         9.42624
        0.00014,         0.00033,        11.29858

This proves that the minus index has the O(n) complexity as x[len(x)-1], apparently, x[-1] runs faster than x[len(x)-1] since the second way requires the running of len() function.
This mainly proves that my method is better than Authors solution.

Olus this is the first Running Test Case I have designed.
"""
