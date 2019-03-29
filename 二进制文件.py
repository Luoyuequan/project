while True:
    Str=input('请输入文本内容：')

    for i in range(len(Str)):
        s=ord(Str[i])
        a=chr(s)
        f=open('text.txt','a')
        f.write(str(a)+'对应的ASCII码为：'+str(s)+'\n')
        f.close();
