#Yes, this is the correct code. 
#Look closely: the else clause belongs to the for loop, not the if statement.


def find_prime(number1):
    
    for n in range(2,number1):
        for k in range(2,n):
            if n % k == 0:
                print n, 'is not a prime'
                # Once found it, quit this loop immediately.
                break
        # attention here!!!
        else:
                print n, 'is a prime'
                
                

find_prime(10)
        