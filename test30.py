# coding: UTF-8
# test decrator

import functools

def callinfo(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'begin call'
		return func(*args, **kw)
	return wrapper

@callinfo
def add(a, b):
	return a+b

num = add(3, 4)
print num
