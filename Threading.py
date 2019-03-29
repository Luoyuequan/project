import threading
import time
lock=threading.Lock()#创建一个指令锁;
number=0;
def Print():
    global number
    if lock.acquire():
        print('%s 获得指令锁\n'%threading.currentThread().getName(),end="");
        b=number
        number=b+1;
        print(str(number)+'\n',end='')
        time.sleep(0.001)
        print('%s 释放指令锁\n'%threading.currentThread().getName(),end="");
        lock.release();#释放

    
for i in range(20):
    T=threading.Thread(target=Print)#声明线程，调用函数，输入参数
    T.setDaemon(True);#守护线程
    T.start();#调用线程，启动
T.join();#阻塞进程，等待线程结束
print(number);
