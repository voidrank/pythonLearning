import smtplib
import sys, os, string, ConfigParser
import email.mime.text

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
msg = email.mime.text.MIMEText("There is a Comment")
msg["Subject"] = "There is a Comment"
print msg.as_string()
smtp.sendmail(from_addr, to_addrs, msg.as_string())
smtp.quit()
