from tkinter import *
from tkinter.messagebox import *

def press(event):
    print('按下'+event.char);
def show(event):
    showinfo(title='标题',message="你按下"+event.char)
win=Tk();
t=Text(win);
t.bind('<Key>',press)

t.pack();

win.bind('<Key>',show)
win.mainloop()
