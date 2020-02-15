#！ /usr/bin/env python
#  -*- coding: utf-8 -*-
# __author__:"yestolife"
# github:https://github.com/yestolife

#将目录下的nCov_Data.pdf作为附件发送邮件给指定邮箱，实现邮件订阅消息

import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def send_email_fun():
    # 第三方 SMTP 服务配置
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "test4python@163.com"  # 用户名
    mail_pass = "qwer1234"  # 口令
    sender = 'test4python@163.com'
    receivers = ['test4python@163.com']
    message = MIMEMultipart()
    message['From'] = Header("Andy", 'utf-8')
    message['To'] = Header("Andy", 'utf-8')
    subject = '订阅疫情信息'
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText('订阅疫情信息见附件pdf', 'plain', 'utf-8'))
    # 构造附件，传送当前目录下的 nCov_Data.pdf文件
    att1 = MIMEText(open('nCov_Data.pdf', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="nCov_Data.pdf"'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()#smtp对象构造
        smtpObj.connect(mail_host, 25)  # 连接第三方smtp服务器，25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)#登入第三方smtp服务器
        smtpObj.sendmail(sender, receivers, message.as_string())#发送邮件
        os.remove("nCov_Data.pdf")#邮件发送成功后删除已发送的pdf，避免下一次读写pdf时出错
        print("邮件发送完成")
    except smtplib.SMTPException:
        print("无法发送邮件")