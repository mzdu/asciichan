import re

f = open('test.txt', 'r')
strings = re.findall(r'\w+\sand\s\w+', f.read())

print strings