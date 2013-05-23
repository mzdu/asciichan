# character and integer mutual exchange

print ord('a')

print chr(98)

#repr outputs a raw format 'a' instead of a
print repr(chr(97))

# unichr() output a character with the unicode of 8224
print unichr(8224)

# Use map(), follows ord rules, and output a list
print map(ord, 'abcd')

# join() can connect the contents of a list with specified character
print ''.join(map(chr, range(97, 100)))