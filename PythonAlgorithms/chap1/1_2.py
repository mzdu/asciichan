# You need to turn a character into its numeric ASCII or Unicode code, and vice versa.

# ord() chr() repr() unichr()

print ord('a')   # 97  ASCII   ord() converts a letter to an ASCII number

print chr(97)    # a   chr(xx)  converts an ASCII number to a character.
print repr(chr(97))    # 'a'

print ord(u'\u2020')  # 8224

print unichr(8224)   # this will generates a cross
print repr(unichr(8224))  # u'\u2020'