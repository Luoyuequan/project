import smtplib,time,os
from time import *
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import *

fromaddr='1260612638@qq.com'
smtp_qq='smtp.qq.com'#服务器
smtp_ID='1260612638'#账户
smtp_passwd='icyeitjwfmmlijfc'#授权码
smtp_port=587#端口号
#变量
#content_i=0
#title_i=0
#输入收件人地址、发送次数
toaddr=input('请输入收件人邮箱地址,如(*******@qq.com):')
Title=input('请输入邮件标题:')
#Content=input('请输入发送邮件内容:')
#************程序开始循环运作***********************
while True:
    try:
        #if title_i>=int(number):
        #    print('******************结束邮件发送******************')
        #    break;
    #os.system('cls')
    #s=input('输入s进入邮件编辑,输入q退出邮件：')
        print('加载2秒....')
        sleep(2)
        print('开始发送....')
        #content_i+=1
        #title_i+=1
#邮件内容编辑
        content='''
            邮件测试-文件版
            '''
#邮件标题编辑
        #title='测试%d号'%(title_i)
#邮件内容、发件人、收件人、标题
        msg = MIMEMultipart()
        #邮件正文内容
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 text.txt 文件
        att1 = MIMEText(open('text.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment;filename="罗.txt"'
        msg.attach(att1)
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = Header(Title, 'utf-8')
#连接邮件服务器
        SMTP_QQ= smtplib.SMTP(smtp_qq,smtp_port)
        SMTP_QQ.starttls();
    #验证登录
        SMTP_QQ.login(smtp_ID,smtp_passwd)
    #开始发送
        SMTP_QQ.sendmail(fromaddr,toaddr,msg.as_string())
            
        SMTP_QQ.close();
        print('******************邮件发送成功******************')
    except(gaierror,error,herror,smtplib.SMTPException) as e:
        print(e)
        break;
