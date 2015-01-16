#!/usr/bin/python2
# coding: UTF-8

#rewrite MyLoginSystem using sqlite rather than serialization (i.e. pickle)

# register an login system simulation, use md5 or sha1 to encode password

import hashlib
import os
import sqlite3

AccountTail = "Add_Salt"

def get_pre_code(account, password):
	return password + account + AccountTail

def login(account, password):
	md5 = hashlib.md5()
	md5.update(get_pre_code(account, password))
	value = md5.hexdigest()
	#print value

	cursor.execute("select * from AccountTable where Account='%s'" %account)
	result = cursor.fetchone()#fetchall()
	#print result

	if result:
		return result[1] == value
	else:
		return False

def register(account, password):
	cursor.execute("select * from AccountTable where Account='%s'" %account)
	result = cursor.fetchall()
	#print result
	if result:
		return -1	#already registered

	md5 = hashlib.md5()
	md5.update(get_pre_code(account, password))

	cursor.execute("insert into AccountTable values('%s', '%s')" %(account, md5.hexdigest()))
	conn.commit()
	return 0

#判断表不存在则创建表
#method 1: 'create table if not exists MessageLogTable_2 (ID integer primary key, name varchar(20))'
#method 2: 'select count(*) from sqlite_master where name = \'AccountPassword\''

conn = sqlite3.connect('LoginSystemAccount.db')
cursor = conn.cursor()
cursor.execute('create table if not exists AccountTable (Account varchar(20) primary key, PassWord varchar(20))')
conn.commit()

while True:
	choose = raw_input("input \'1\' to login, \'2\' to register, and \'q\' to quit: ")
	if choose == '1':	#login
		account = raw_input("input your account: ")
		password = raw_input("input your password: ")
		if login(account, password):
			print "login succed, welcome"
			break
		else:
			print "login faild"

	elif choose == '2':	#register
		account = raw_input("input your account: ")
		password1 = raw_input("input your password: ")
		password2 = raw_input("input your password again: ")
		if (password1 != password2):
			print "your password not match"
			continue
		ret = register(account, password1)
		if ret == 0:
			print "register succed"
			#break
		elif ret == -1:
			print "register failed: this account has already exist"
		else:
			print "register failed"
	elif choose == 'q':	#quit
		print "byebye!"
		break

print "program exit"
