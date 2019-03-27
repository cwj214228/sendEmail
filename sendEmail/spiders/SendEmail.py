import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self):
        self.email_host = 'smtp.qq.com'
        self.email_port = '465'
        self.email_sender = '1343500013@qq.com'
        self.email_receiver = '1251629640@qq.com'
        self.email_password = 'elkafxknrpeshefg'

        # 发送纯文本邮件
        # body 为字符串

    def send_text_email(self, body, receiver, subject):
        # 1.内容主体
        # 2.内容类型
        # 3.编码方式
        message_text = MIMEText(body, 'plain', 'utf-8')
        message_text['From'] = self.email_sender
        message_text['To'] = receiver
        message_text['Subject'] = subject

        try:
            email_client = smtplib.SMTP_SSL(self.email_host, self.email_port)
            login_result = email_client.login(self.email_sender, self.email_password)
            print('开始登录', login_result)
            # 如果有登录信息 而且登录信息里面第一条状态码为235说明登陆成功
            if login_result and login_result[0] == 235:
                print('登录成功')
                email_client.sendmail(self.email_sender, receiver, message_text.as_string())
                print('发送完成')
            else:
                print('登录失败')
        except Exception as e:
            print('邮件发送失败', e)
