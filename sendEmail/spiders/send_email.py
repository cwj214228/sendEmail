# -*- coding: utf-8 -*-
import scrapy


from sendEmail.spiders.SendEmail import SendEmail


class SendEmailSpider(scrapy.Spider):
    name = 'send_email'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']


    def parse(self, response):
        email = SendEmail()
        subject = '发送邮件的主题'
        body = '邮件的内容'
        receiver = '1251629640@qq.com'
        email.send_text_email(body, receiver, subject)




