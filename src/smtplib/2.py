# -*- coding: utf-8 -*-
import smtplib
import json
import sys, os, string, ConfigParser
import email.mime.text


l = json.load(open("uids.json","r"))
for i in l:
	conf = ConfigParser.ConfigParser()
	conf.read("stmp.conf")

	username=conf.get("user_info", "username")
	from_addr=conf.get("user_info","username")
	to_addrs=[conf.get("user_info", "to_addrs")]
	password=conf.get("user_info", "password")
	HOST=conf.get("server_info", "HOST")
	PORT=conf.get("server_info", "PORT")


	#Create SMTP object
	smtp = smtplib.SMTP()
	print "connecting .."

	#Show the debug log
	smtp.set_debuglevel(1)

	#Connect
	try:
		print smtp.connect(HOST,PORT)
	except:
		print "CONNECT ERROR *****"

	#126 uses ssl
	smtp.starttls()

	try:
		print "loginning ..."
		smtp.login(username, password)
	except:
		print "LOGIN ERROR ****"
# fill content with MINEText's object
	msg = email.mime.text.MIMEText("技科一班的同学，想去春游吗？登录psycium.xyz:8081/来为你想去的地方投票吧！你的uid是:%s 密码是%s" % (i['uid'].encode('utf-8'), i['passwd'].encode('utf-8')), "html", "utf-8")
	#% (i['uid'],i['passwd']))
	msg["Subject"] = "技术科学实验班一班秋游地点投票！！！！"
	print msg.as_string()
	smtp.sendmail(from_addr, i["uid"]+"@fudan.edu.cn", msg.as_string())
smtp.quit()

