#coding:utf8
import threading
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_info = {
    "from": "857377352@qq.com",
    "to": "971935832@qq.com",
    "hostname": "smtp.qq.com",
    "username": "857377352@qq.com",
    "password": "mlrrjhqiojrlbbeh",
    "mail_subject": "test",
    "mail_text": "hello, this is a test email, sended by py",
    "mail_encoding": "utf-8"
}

# if __name__ == '__main__':
#这里使用SMTP_SSL就是默认使用465端口
def sendmailfunc():
	smtp = SMTP_SSL(mail_info["hostname"])
	smtp.set_debuglevel(1)

	smtp.ehlo(mail_info["hostname"])
	smtp.login(mail_info["username"], mail_info["password"])

	msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
	msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
	msg["from"] = mail_info["from"]
	msg["to"] = mail_info["to"]

	smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

	smtp.quit()

	print("send success")
	threading.Timer(1,sendmailfunc).start()

sendmailfunc()