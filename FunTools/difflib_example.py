import difflib

text1, text2 = ['identity', 'social', 'life', 'psychology'], ['identity', 'psychology']


d = difflib.Differ()
result = list(d.compare(text1, text2))
print result

# produce the compared result, if not diff, no change, if delete, starts with '- ', if add, '+ '