numbers=1#行数


'''
while numbers <= 5:
    for index in range(numbers):
        print('*',end='')

    print('')
    numbers+=1
'''

'''
000*000
00***00
0*****0
*******
'''
# last=11#最中间一排星星数量
last = int(input('请输入奇数:'))
tao = int(input('掏空数量:'))
for a in range(1,tao+1):
    if a % 2 != 0:
        print(a)
for i in range(1,last+1):
    
    if i % 2 != 0:
        blocks=int((last-i)/2)#空格数量
        #print(blocks)
        for a in range(blocks):
            print(' ',end='')
        for j in range(i):
            print('#',end='')
            
        print('')
    if i == last:
        down=last-2;
        while down >= 1:
            if down % 2 != 0:
                dblocks=int((last-down)/2)#空格数量
                #print(blocks)
                for a in range(dblocks):
                    print(' ',end='')
                for j in range(down):
                    print('#',end='')
                print('')
                down-=2
                
'''
*
**
***
****
***
**
*
rows=9;
i=1;
while rows <= 1:
'''  
