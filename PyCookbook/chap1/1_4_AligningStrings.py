# You want to align your strings left, center and right.

print '|'+'hello'.ljust(10)+'|','her'.rjust(20),'|','hec'.center(40),'|'
#'hello'.ljust(10) generates a space with the length of 10
# Pay attention on the different connectors ',' VS '+'
# Comma actually will generates an extra space after it, but '+' will directly connect them while adding extra space.

# if the length of string is longer than the space what will happen?
print "hellokitty".ljust(2)
# this will not cause any error, it is just a bit of tight.


# we could also change the space to other symbols
print 'hellokitty'.center(20, '+')             
# Console: +++++hellokitty+++++

