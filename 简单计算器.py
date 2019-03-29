from tkinter import *

root = Tk()
root.title('计算器');
root.geometry('250x200')

m=StringVar()
en1=StringVar();
en2=StringVar();
en3=StringVar();
a=StringVar();
A='+';
B='-';
C='*';
D='//';
E='**';
F='%';
m1=Menu(root)
m2=Menu(m1)
def Print1():
    a.set('+');
def Print2():
    a.set('-');
def Print3():
    a.set('*');
def Print4():
    a.set('//');
def Print5():
    a.set('**');
def Print6():
    a.set('%');
def Print7():
    if (a.get()==str(A)):
        en3.set(float(en1.get())+float(en2.get()));
    elif (a.get()==str(B)):
        en3.set(float(en1.get())-float(en2.get()));
    elif (a.get()==str(C)):
        en3.set(float(en1.get())*float(en2.get()));
    elif (a.get()==str(D)):
        en3.set(float(en1.get())//float(en2.get()));
    elif (a.get()==str(E)):
        en3.set(float(en1.get())**float(en2.get()));
    elif (a.get()==str(F)):
        en3.set(float(en1.get())%float(en2.get()));
m2.add_radiobutton(label="加法运算",command=Print1,variable=m)
m2.add_radiobutton(label="减法运算",command=Print2,variable=m)
m2.add_radiobutton(label="乘法运算",command=Print3,variable=m)
m2.add_radiobutton(label="整除法运算",command=Print4,variable=m)
m2.add_radiobutton(label="幂运算",command=Print5,variable=m)
m2.add_radiobutton(label="求模运算",command=Print6,variable=m)
m1.add_cascade(label='基础运算法则',menu=m2)

root['menu']=m1

l1=Label(root,text='简单计算器',fg='red').place(x=90,y=5)

entry1=Entry(root,width=8,textvariable=en1);
entry1.place(x=5,y=30);
#entry1.bind("<FocusIn>",FocusIn);

l=Label(root,text=str(a),textvariable=a).place(x=65,y=28)
a.set('+')

entry2=Entry(root,width=8,textvariable=en2);
entry2.place(x=85,y=30);

Button(root,text='=',command=Print7).place(x=148,y=27)

entry3=Entry(root,width=10,textvariable=en3);
entry3.place(x=170,y=30);






root.mainloop();

