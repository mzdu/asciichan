
# My Third Attempt
def intToString(number):
    numStr = '0123456789'
    if number != 0:
        return intToString(number//10) + numStr[number%10]
    else:
        return ''


print intToString(456456463121) + ' done'

# My Second Attempt
'''
def intToString(number):
    
    if number != 0:
        return intToString(number//10) + str(number%10) 
    else:
        return ''





Summary:
1. if you are using recursion, the recursion itself will at least reduce one for loop
2. you have to figure out an exit for the program, such as else: return ''
3. Pay attention on the difference between '//' and '/', 123//10 == 123/10, whereas, 123.4 // 10 = 12, 123.4 / 10 = 12.34
4. Try to implement without str() function.
'''



# My first attempt, we should use recursion and if else to replace the for or while loop
'''
def intToString(number):
    while number != 0:
        digit = number % 10
        number = number / 10
        
        intToString(number)
    return str(digit)

print intToString(number)

'''