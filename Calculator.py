from tkinter import *

root = Tk()
root.geometry('300x350')

frame = Frame(root,bd=2,relief=GROOVE,bg='#515151')
frame.pack()
Resultframe = Frame(frame,bd=2,relief=GROOVE,bg='#515151')
Resultframe.pack()
Number = Frame(frame,bg='#515151')
Number.pack()

for i in range(4):
    Number.grid_rowconfigure(i, pad=1)

for i in range(4):
    Number.grid_columnconfigure(i, pad=1)


result = StringVar()

expression = ""

ResultLabel = Label(Resultframe,textvariable=result,width=35).pack()

def press(num):
    global expression
    expression += str(num)
    result.set(expression)

Bdot = Button(Number,text='.', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT)
Bdot.grid(row=4,column=2)
B0 = Button(Number,text='0', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(0))
B0.grid(row=4,column=1)
B1 = Button(Number,text='1', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(1))
B1.grid(row=3,column=1)
B2 = Button(Number,text='2', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(2))
B2.grid(row=3,column=2)
B3 = Button(Number,text='3', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(3))
B3.grid(row=3,column=3)
B4 = Button(Number,text='4', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(4))
B4.grid(row=2,column=1)
B5 = Button(Number,text='5', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(5))
B5.grid(row=2,column=2)
B6 = Button(Number,text='6', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(6))
B6.grid(row=2,column=3)
B7 = Button(Number,text='7', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(7))
B7.grid(row=1,column=1)
B8 = Button(Number,text='8', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(8))
B8.grid(row=1,column=2)
B9 = Button(Number,text='9', font=('Bahnschrift', 10 ),width=8,height=2,bg='#101010',fg="#f1f1f1",relief=FLAT,command=lambda: press(9))
B9.grid(row=1,column=3)


Bdivide = Button(Number,text='%', font=('Bahnschrift', 10 ),width=8,height=2,bg='#313131',fg="#f1f1f1",relief=FLAT)
Bdivide.grid(row=1,column=4)
Bmultiply = Button(Number,text='*', font=('Bahnschrift', 10 ),width=8,height=2,bg='#313131',fg="#f1f1f1",relief=FLAT)
Bmultiply.grid(row=4,column=3)
Bsub = Button(Number,text='-', font=('Bahnschrift', 10 ),width=8,height=2,bg='#313131',fg="#f1f1f1",relief=FLAT)
Bsub.grid(row=3,column=4)
Bplus = Button(Number,text='+', font=('Bahnschrift', 10 ),width=8,height=2,bg='#313131',fg="#f1f1f1",relief=FLAT)
Bplus.grid(row=2,column=4)


def Hover(button, color1, color2):
    button.bind("<Enter>", func=lambda e: button.config(background=color1))
    button.bind("<Leave>", func=lambda e: button.config(background=color2))

Bequal = Button(Number,text='=', font=('Bahnschrift', 10 ),width=8,height=2,bg='#14476D',fg="#f1f1f1",activebackground='#14476C',relief=FLAT)
Bequal.grid(row=4,column=4)

Button_list = [B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,Bdivide,Bmultiply,Bsub,Bplus]

########HOVERING#########
for item in range(len(Button_list)):
    Hover(Button_list[item], '#3F3F3F', '#101010')

Hover(Bequal, '#1A5BAE', '#14476D')


root.mainloop()
