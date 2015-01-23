#!/usr/bin/python2
# coding: UTF-8

# test for getting activation keys, enhanced with saving keys to sqlite3

import random
import sqlite3

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

conn = sqlite3.connect('KeyGen.db')
cursor = conn.cursor()
cursor.execute('create table if not exists KeysTable (Key varchar(20) primary key)')
cursor.execute('select * from KeysTable')
result = cursor.fetchall()
print result, len(result)
if result:
	input = raw_input("There's already %d keys in Database, do you still want to save these new keys? (Y/N)" %len(result))
	if input != 'Y':
		print "Keys not saved"
	else:
		for key in KeyList:
			cursor.execute("insert into KeysTable values('%s')" %key)
		print "Keys saved"
else:
	for key in KeyList:
		cursor.execute("insert into KeysTable values('%s')" %key)
	print "Keys saved"

conn.commit()



