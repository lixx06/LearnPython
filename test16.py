#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# register an login system simulation, use md5 or sha1 to encode password

import hashlib
import os
try:
	import cPickle as pickle
	print "cPickle module imported"
except ImportError:
	import pickle
	print "picled module imported"

AccountTable = dict()
SaveAccountDataPath = "AccountData.txt"
AccountTail = "Add_Salt"

def get_pre_code(account, password):
	return password + account + AccountTail

def login(account, password):
	md5 = hashlib.md5()
	md5.update(get_pre_code(account, password))
	value = md5.hexdigest()
	#print value
	if AccountTable.get(account):	
		return AccountTable.get(account) == value
	return False

def register(account, password):
	if account in AccountTable:
		return -1
	md5 = hashlib.md5()
	md5.update(get_pre_code(account, password))
	AccountTable[account] = md5.hexdigest()
	return 0

try:
	fp = open(SaveAccountDataPath, "rb")
	AccountTable = pickle.load(fp)
	fp.close
except IOError:	#首次运行程序
	pass


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

fp = open(SaveAccountDataPath, "wb")
pickle.dump(AccountTable, fp)
fp.close
print "program exit"
