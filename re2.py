import re
 
s = 'google.com'
 
match = re.search(r'.', s)
print(match)
 
match = re.search(r'\.', s)
print(match)