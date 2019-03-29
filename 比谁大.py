from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('比谁大');

def press(event):
    if e.get().isdigit()==False:
        showerror(title="错误",message="请不要输入含有特殊符号、中文、英文的字符");

def callback():
    a=int(e.get())+1;
    showinfo(title='结果',message='我的数值比你大为'+str(a))

frame=Frame(root,width='300',height='200',bg='black')

label=Label(frame,text='与程序比大小',fg='red',bg='black').pack(pady=10)
label1=Label(frame,text='请在下方文本框中输入数字',fg='white',bg='black').pack()

e=StringVar();
entry=Entry(frame,textvariable=e)

entry.bind("<Leave>",press)
entry.pack(pady=10)

button=Button(frame,command=callback,text="生成数字")

button.pack(pady=10);

frame.pack(ipadx=10,ipady=10)

root.mainloop();
