from tkinter import *

win=Tk();
win.title('签到')
l_1=StringVar()
l_2=StringVar()
Label(win,text='班级：').grid(row=0,column=0)
Label(win,text='名字：').grid(row=1,column=0)
Entry(win,width=20,textvariable=l_1).grid(row=0,column=1)
Entry(win,width=20,textvariable=l_2).grid(row=1,column=1)
Button(win,text='点击签到').grid(row=2,column=0,columnspan=2)

win.mainloop()
