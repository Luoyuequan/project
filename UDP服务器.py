import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=8001;
host='10.1.57.180'
s.bind((host,port));
while True:
    print('等待对方发送内容')
    data,addr=s.recvfrom(1024)
    print(data.decode('utf-8'),addr[0])
s.close();
