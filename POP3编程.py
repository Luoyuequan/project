from poplib import *
from getpass import getpass
from socket import *
from time import *

pop3svr='pop.qq.com'
port=110
username=input('请输入用户名：')
password=input('输入密码：')

try:
    recvsvr=POP3(pop3svr)
    try:
        recvsvr.user(username)
        recvsvr.pass_(password)
        ret=recvsvr.stat()
        for i in range(1,ret[0]+1):
            print(recvsvr.top(i,0))
        recvsvr.quit();
    except error_proto as e:
        print(e)
except(gaierror,error,herror) as e:
    print(e)
    sleep(5)
#qxjpotnkxzkvgecf
