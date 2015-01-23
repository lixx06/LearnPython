#!/usr/bin/python2
# coding: UTF-8

# test for getting activation keys

import random

#SourceDict and KeyLens can be modified
SourceDict = map(chr, (range(ord('A'), ord('Z') + 1)))
KeyLen = 15
KeyNum = 200

print SourceDict

KeyList = list()
for i in range(KeyNum):
	ThisKey = str()
	for j in range(KeyLen):
		index = random.randint(0, len(SourceDict) - 1)
		ThisKey += SourceDict[index]
	KeyList.append(ThisKey)

print KeyList

