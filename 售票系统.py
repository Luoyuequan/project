from tkinter.messagebox import *
import os
from time import *
list_1=[['未售','未售','未售','未售','未售','未售','未售','未售'],
        ['未售','未售','未售','未售','未售','未售','未售','未售'],
        ['未售','未售','未售','未售','未售','未售','未售','未售'],
        ['未售','未售','未售','未售','未售','未售','未售','未售']]
while(True):
    os.system('cls');
    print('\t\t\t\t售票中心')
    for i in range(len(list_1)):
        for j in range(len(list_1[i])):
            print('\t'+str(i)+'-'+str(j),end='')
        print();
        for j in range(len(list_1[i])):
            print('\t'+list_1[i][j],end='');
        print()
    str_1=input('请输入数字购买车票如(12),或输入q退出:')
    if(str_1=='q'):
        print('\t\t欢迎下次光临,拜拜~~')
        sleep(3);
        break;
    for i in range(len(list_1)):
        for j in range(len(list_1[i])):
            if(str_1==str(i)+str(j)):
                if(list_1[i][j]!="已售"):
                   list_1[i][j]="已售"
                   print('\t\t正在购买中...')
                   sleep(2)
                   print('\t\t'+str(i)+'-'+str(j)+'号票已购买')
                   print('\t\t'+strftime('%Y-%m-%d %H:%M:%S',localtime())+' 星期'+strftime('%w',localtime()))
                   sleep(1.5)
                else:
                   print('\t\t提示,此票号已售出!!');
                   sleep(3)
        
