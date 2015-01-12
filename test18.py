#!/usr/bin/python2
# coding: UTF-8
# 迭代器

import itertools

#help(itertools)
#help(itertools.count)

nature = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, nature)
for n in ns:
	print n

print "over"

for c in itertools.chain('ABC', 'DEF'):
	print c