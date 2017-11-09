# coding:utf-8

import logging
import setting
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class Email_Send_Module():
    def __init__(self):
        email_config = setting.EMAIL_CONFIG
        self.__sender = email_config['sender']
        self.__receiver = email_config['receiver']
        self.__subject = email_config['subject']
        self.__smtpserver = email_config['smtpserver']
        self.__username = email_config['username']
        self.__password = email_config['password']
        self.__files = email_config['files']
        logging.debug(email_config)

    def PostEmail(self):
        sender = self.__sender
        receiver = self.__receiver
        subject = self.__subject
        smtpserver = self.__smtpserver
        username = self.__username
        password = self.__password
        files = self.__files

        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = subject
        text_msg = MIMEText(
            "<html><body><p><span style='color: red;'>&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp; "
            "附件为本次回归的测试报告，请各位查收。<br/></p></body></html>",
            'html', _charset="utf-8")
        text_msg['Subject'] = Header(subject, 'utf-8')
        msgRoot.attach(text_msg)

        # 附件
        att = MIMEText(open(files, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="report.html"'
        msgRoot.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        # smtp.esmtp_features["auth"]="LOGIN PLAIN"
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()


if __name__ == '__main__':
    P = Email_Send_Module()
    P.PostEmail()
