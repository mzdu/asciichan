import re
'''
In python, a regular expression search is written as:
match = re.search(pat, str)

'''

str = 'an example word:cat!!! one = 1, two = 2'

# stores the search result in a variable named "match"
# search(r....), r designates a python 'raw' string

# # match = re.search(r'word:\w\w\w', str)
# #  
# # match = re.search(r'..t!', str)
# # 
# # match = re.search(r'\w\w\w\s=\s\d', str)
# # 
# # match = re.search(r'\w\w\w', '@@@he,go')
# # 
# # match = re.search(r'^b\w+', 'basketballll$')

str1 = 'dfa dfd Name: dan, Email: dan-p@email.sc.edu, Name: Sharif, Email: Sha@google.com, jla;jkajdfkdjfdkf'

#findall() finds all strings that matches
matches = re.findall(r'[\w.-]+@[\w.-]+', str1)

if matches:
    for match in matches:
        print match
    
else:
    print 'did not find'
    
    
