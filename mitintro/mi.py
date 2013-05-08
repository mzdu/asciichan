# Calculate a**b with log(n) complexity
a, b =0, 0

def func0(a, b):
    # complexity is O(n)
    sum = 1
    while b > 0:
        sum = sum * a
        b -= 1
    return sum

def func1(a, b):
    if b == 1:
        return a
    else:
        return a * func1(a, b-1)

# Video Lec8 16:00
def func2(a, b):
    if b == 1:
        #Everybody needs an exit.
        return a
    else:
        if b % 2 == 0:
            #Even Case
            return func2((a*a), b/2)
        else:
            #Odd Case
            return a * func2(a, b-1)


print func0(2, 4)        

print func1(2, 4)

print func2(2, 4)