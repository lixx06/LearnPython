
import re
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
	print "match 1"
if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
	print "match 2"

str1 = 'a b   c'
str2 = 'a,b  c,d e;  ; f'
str1.split(" ")
print re.split(r'\s+', str1)
print re.split(r'[\s\,\;]+', str2)
