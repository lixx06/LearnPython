
import pdb

def is_odd(n):
	return (n % 2 == 1)

a = range(1, 11)
print a
b = filter(is_odd, a)
print b



import pack1.cal
print pack1.cal.add(3, 5)



import mod2
s1 = mod2.Student("lixx", 100)
s1.printscore()
s1.modscore(99)

pdb.set_trace()

s1.printscore()
s1.modscore(98)
s1.printscore()

s1.get_spec_name()
print s1._Student__name
print s1.__name

