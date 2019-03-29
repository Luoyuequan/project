import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=8001;
host='10.1.57.180'
while True:
    content=input('请输入内容：')
    s.sendto(content.encode('utf-8'),(host,port))
s.close();
