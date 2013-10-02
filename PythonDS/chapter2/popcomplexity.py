import timeit

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print popzero.timeit(number=1000)


x = list(range(2000000))
print popend.timeit(number=1000)

# this proves pop() is much faster than pop(0), but it does not validate the claim that
# pop0 is O(n) while pop() is O(1)

# popcomplexity2.py implements this test.