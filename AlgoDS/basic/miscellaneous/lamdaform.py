def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print f(0) #42

print f(1) #43

print f(0) #42
