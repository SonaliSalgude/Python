import re
 
s = 'Kolhapur: D.Y. Patil College of engineering'
 
match = re.search(r'Patil', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())