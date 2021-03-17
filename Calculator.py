from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

root = Tk()
root.geometry('300x350')
style = ThemedStyle(root)
style.set_theme("arc")

frame = Frame(root,bd=2,relief=GROOVE)
frame.pack()
Resultframe = Frame(frame,bd=2,relief=GROOVE)
Resultframe.pack()
Number = Frame(frame)
Number.pack()


result = StringVar()

expression = ""

ResultLabel = Label(Resultframe,textvariable=result,width=35).pack()

def press(num):
    global expression
    expression += str(num)
    result.set(expression)

Bdot = ttk.Button(Number,text='.',width=7)
Bdot.grid(row=4,column=3)
B0 = ttk.Button(Number,text='0',width=7,command=lambda: press(0))
B0.grid(row=4,column=1)
B1 = ttk.Button(Number,text='1',width=7,command=lambda: press(1))
B1.grid(row=3,column=1)
B2 = ttk.Button(Number,text='2',width=7,command=lambda: press(2))
B2.grid(row=3,column=2)
B3 = ttk.Button(Number,text='3',width=7,command=lambda: press(3))
B3.grid(row=3,column=3)
B4 = ttk.Button(Number,text='4',width=7,command=lambda: press(4))
B4.grid(row=2,column=1)
B5 = ttk.Button(Number,text='5',width=7,command=lambda: press(5))
B5.grid(row=2,column=2)
B6 = ttk.Button(Number,text='6',width=7,command=lambda: press(6))
B6.grid(row=2,column=3)
B7 = ttk.Button(Number,text='7',width=7,command=lambda: press(7))
B7.grid(row=1,column=1)
B8 = ttk.Button(Number,text='8',width=7,command=lambda: press(8))
B8.grid(row=1,column=2)
B9 = ttk.Button(Number,text='9',width=7,command=lambda: press(9))
B9.grid(row=1,column=3)


Bdivide = ttk.Button(Number,text='%',width=7)
Bdivide.grid(row=1,column=4)
Bmultiply = ttk.Button(Number,text='x',width=7)
Bmultiply.grid(row=2,column=4)
Bsub = ttk.Button(Number,text='-',width=7)
Bsub.grid(row=3,column=4)
Bplus = ttk.Button(Number,text='+',width=7)
Bplus.grid(row=4,column=4)

Bequal = ttk.Button(Number,text='=',width=40)
Bequal.grid(row=6,column=1,columnspan=4)


root.mainloop()
