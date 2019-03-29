from tkinter import *

win = Tk()
win.title('函数图像')
win.geometry('600x600')
top = Menu(win)
top_1 = Menu(top)
top_1.add_command(label='ｘ〓ｙ', )
top_1.add_command(label='ｘ＾(α)〓ｙ', )
top_1.add_command(label='ａ＾(ｘ)〓ｙ', )
top.add_cascade(label='函数图像', menu=top_1)
win['menu'] = top
# Label(win,text='请输入数据:',).grid(row=0,column=0);
# Entry(win,).grid(row=0,column=1)

X = Label(win, text='Ｘ')
X.place(x=300, y=165)
Y = Label(win, text='Ｙ')
Y.place(x=145, y=0)
Label(win, text='ｘ=ｙ').place(x=300, y=0)
cv = Canvas(win, width=300, height=300, bg='white')
cv.create_line(0, 150, 300, 150, arrow='last')
cv.create_line(150, 300, 150, 0, arrow='last')
cv.create_line(300, 0, 0, 300)

cv.place(x=0, y=20)
win.mainloop();
