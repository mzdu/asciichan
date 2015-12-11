a = []
for i in range(10):
    print 'i is', i
    a.append(i*i)
    print "a is", a

for sth in a:
    print "sth", sth

print 'i is', i

for a[i] in a:
    print "i in a[i], i is ", i
    print "a is", a

# OUTPUT:
# i is 0
# a is [0]
# i is 1
# a is [0, 1]
# i is 2
# a is [0, 1, 4]
# i is 3
# a is [0, 1, 4, 9]
# i is 4
# a is [0, 1, 4, 9, 16]
# i is 5
# a is [0, 1, 4, 9, 16, 25]
# i is 6
# a is [0, 1, 4, 9, 16, 25, 36]
# i is 7
# a is [0, 1, 4, 9, 16, 25, 36, 49]
# i is 8
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64]
# i is 9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# sth 0
# sth 1
# sth 4
# sth 9
# sth 16
# sth 25
# sth 36
# sth 49
# sth 64
# sth 81
# i is 9
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 0]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 1]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 4]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 9]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 16]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 25]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 36]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 49]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 64]
# i in a[i], i is  9
# a is [0, 1, 4, 9, 16, 25, 36, 49, 64, 64]
