# coding: UTF-8

def gen_squar(n):
	for i in range(n):
		yield i ** 2

for i in gen_squar(6):
	print i,
