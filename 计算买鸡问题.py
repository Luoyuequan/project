x=range(1,22)
y=range(1,33)
for i in range(len(x)):
    for j in range(len(y)):
        if(int(200-14*(x[i])-8*(y[j]))==0):
            print('公鸡的数量:%d,母鸡的数量:%d,'%(x[i],y[j]),end='');
            Number=100-(x[i]+y[j])
            print('小鸡:%d'%(int(Number)))
            money=x[i]*5+y[j]*3+int(Number)/3;
            print("总钱:%d"%(int(money)))
