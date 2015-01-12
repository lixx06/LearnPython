#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# send email

import smtplib
from email.mime.text import MIMEText
#from log import logger

def send_email(receiver, content):
	sender = "lixx06@gmail.com"
	host = "smtp.gmail.com"
	port = 465
	msg = MIMEText(content)
	msg["From"] = ""
	msg["To"] = receiver
	msg["Subject"] = "See my study progress ^_^, and I send this email using python code!"

	try:
		smtp = smtplib.SMTP_SSL(host, port)
		smtp.login(sender, "password")
		smtp.sendmail(sender, receiver, msg.as_string())
		#logger.info
		print("send email success")
	except Exception, e:
		#logger.error
		print(e)

f = open("test16.py", "r")
buf = f.read()
#print buf
SunWen = "362621872@qq.com";
MFL = "592081999@qq.com";
lixx = "651295293@qq.com"
send_email(lixx, buf)
print "email send"

