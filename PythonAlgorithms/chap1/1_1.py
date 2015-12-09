# Problem: You want to process a string one character at a time

def process1(str1):
    list1 = list(str1)
    
    print list1
    

str2 = 'this is a string.'
process1(str2)


print '====================='

list2 = [letter for letter in str2]
print list2

print '====================='

# map(func, list) apply func on every element in list
list3 = map(str, str2)
print list3