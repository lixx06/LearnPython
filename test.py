
import mod1

print "hello world"

print "5+4=", mod1.add(5, 4)

a = range(10)
b = reduce(mod1.add, a)
print a
print b




def char2int(c):
	return {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}[c]

def mul(a, b):
	return 10 * a + b

def str2int(s):
	return reduce(mul, map(char2int, s))

print "test str2int:", str2int("546") * 2 + 1, "=", 546*2+1


