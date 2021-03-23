from tkinter import *
from tkinter import ttk
from math import sqrt as sqrt


#Main window settings
root = Tk()
root.configure(width=300, height=400,bg='#515151')
root.resizable(False, False)
#Window appear at the middle of the screen
posRight = int(root.winfo_screenwidth() / 2 - 300 / 2)
posDown = int(root.winfo_screenheight() / 2 - 385 / 2)
root.geometry("+{}+{}".format(posRight, posDown))
#Remove border
root.overrideredirect(1)

#FUNCTION FOR EACH MODE
def mainMenu():
    hide_frame()
    Menu.pack()

def Basic_mode():
    hide_frame()
    Number.pack()

def Programmer_mode():
    hide_frame()
    P_Number.pack()
    Top_P_Number.pack()
    Bot_P_Number.pack()
    Button_list = [B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,Bdot]
    for item in range(len(Button_list)):
        Hover(Button_list[item], '#3F3F3F', '#212121')

    Hover(P_delete, '#3F3F3F', '#313131')
    Hover(P_Bequal, '#EF6423', '#ff590C')

#FUCNTION THAT HIDE OTHER FRAMES
def hide_frame():
    Menu.pack_forget()
    Number.pack_forget()
    P_Number.pack_forget()

#Frame for Navigation Bar
Navframe = Frame(root,relief=FLAT,bg='#313131',width=300)
Navframe.pack()
#Content of Navigation Bar
Menu = Button(Navframe,text='=', font=('Bahnschrift', 10 ),width=5,height=1,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=mainMenu)
Menu.pack(side=LEFT)
Title = Label(Navframe,text="Calculator", font=('Bahnschrift', 13 ),width=22,height=1,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT)
Title.pack(side=LEFT)
BQuit = Button(Navframe,text='X', font=('Bahnschrift', 10 ),width=5,height=1,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=root.quit)
BQuit.pack(side=RIGHT)


###############MENU MODE###############
#Frame for the Menu Mode
Menu = Frame(root,width=300, height=385,bg='#515151')
#Content
B_Mode = Button(Menu,text='Basic', font=('Bahnschrift', 20 ),width=15,height=2,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=Basic_mode)
B_Mode.grid(row=1,column=0)
P_Mode = Button(Menu,text='Programmer', font=('Bahnschrift', 20 ),width=15,height=2,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=Programmer_mode)
P_Mode.grid(row=2,column=0)

Menu.grid_rowconfigure(1,pad=30)
Menu.grid_rowconfigure(2,pad=30)

###############BASIC MODE###############
#Frame for the Basic Mode
Number = Frame(root,bg='#515151')
Number.pack()

#Variables
result = StringVar()
historic = StringVar()
value1 = StringVar()
value2 = StringVar()
expression = ""
expression2 = ""

#Functions of various buttons for Basic Mode
def press(num):
    global expression

    if num == '-' or num == '+' or num == '/' or num == '.' or num =='*':
        if expression[-1] == '+' or expression[-1] == '-' or expression[-1] == '/' or expression[-1] == '*':
            pass
        else:
            expression += str(num)
    else:
        expression += str(num)
    result.set(expression)

def equal():
    global expression
    main = str(expression)
    historic.set(main)
    total = str(eval(expression))
    result.set(total)
    expression = total

def C():
    global expression
    expression=""
    historic.set("")
    result.set(expression)

def Backspace():
    global expression
    expression = expression[:-1]
    result.set(expression)
    
def delete():
    global expression, expression2
    expression=""
    expression2=""
    value1.set(expression)
    value2.set(expression)


def Hover(button, color1, color2):
    button.bind("<Enter>", func=lambda e: button.config(background=color1))
    button.bind("<Leave>", func=lambda e: button.config(background=color2))
    
#Setting for nice aligned grid
for i in range(7):
    Number.grid_rowconfigure(i, pad=1)

for i in range(4):
    Number.grid_columnconfigure(i, pad=1)

##########Content##########
#BUTTONS
#####WHY LAMBDA########
#IN TKINTER BUTTONS , you can't pass a functions with arguments as tkinter were build like this.
#ex B0 = Buttom(command=press(1))
#But with lambda , we can do it in the button define section.
#Lambda function is used for throw away function or functions to be anonymous as they have no identifier and have a single expression.
#That mean lambda function always return a value
#So we use Lambda here to pass an argument into the function for the buttons
B0 = Button(Number,text='0', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(0))
B0.grid(row=5,column=1)
B1 = Button(Number,text='1', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(1))
B1.grid(row=4,column=1)
B2 = Button(Number,text='2', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(2))
B2.grid(row=4,column=2)
B3 = Button(Number,text='3', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(3))
B3.grid(row=4,column=3)
B4 = Button(Number,text='4', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(4))
B4.grid(row=3,column=1)
B5 = Button(Number,text='5', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(5))
B5.grid(row=3,column=2)
B6 = Button(Number,text='6', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(6))
B6.grid(row=3,column=3)
B7 = Button(Number,text='7', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(7))
B7.grid(row=2,column=1)
B8 = Button(Number,text='8', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(8))
B8.grid(row=2,column=2)
B9 = Button(Number,text='9', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(9))
B9.grid(row=2,column=3)

#Label for results
historicLabel = Label(Number,textvariable=historic,width=39,height=2,fg='#f1f1f1',bg='#515151',anchor='e',justify=RIGHT,font=('Bahnschrift', 10 ),relief=FLAT).grid(row=0,column=1,columnspan=5)
ResultLabel = Label(Number,textvariable=result,width=25,height=2,fg='#f1f1f1',bg='#515151',anchor='e',justify=RIGHT,font=('Bahnschrift', 15 ),relief=FLAT).grid(row=1,column=1,columnspan=5)    
#BUTTONS font , color , size , hovering , command
Bdot = Button(Number,text='.', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("."))
Bdot.grid(row=5,column=2)

#Special Buttons
Bdivide = Button(Number,text='%', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("/"))
Bdivide.grid(row=5,column=4)
Bmultiply = Button(Number,text='*', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("*"))
Bmultiply.grid(row=6,column=4)
Bsub = Button(Number,text='-', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("-"))
Bsub.grid(row=4,column=4)
Bplus = Button(Number,text='+', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("+"))
Bplus.grid(row=6,column=3)
C =  Button(Number,text='C', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=C)
C.grid(row=2,column=4)
Bparenthesis1 = Button(Number,text='(', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("("))
Bparenthesis1.grid(row=6,column=1)
Bparenthesis2 = Button(Number,text=')', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press(")"))
Bparenthesis2.grid(row=6,column=2)
Bequal = Button(Number,text='=', font=('Bahnschrift', 10 ),width=9,height=3,bg='#ff590C',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=equal)
Bequal.grid(row=7,column=4)
Bbackspace = Button(Number,text='Del', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=Backspace)
Bbackspace.grid(row=3,column=4)
Bpowtwo = Button(Number,text='^2', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("**2"))
Bpowtwo.grid(row=7,column=1)
Bpow = Button(Number,text='^', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("**"))
Bpow.grid(row=7,column=2)
Bsqrt = Button(Number,text='sqrt', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: press("sqrt("))
Bsqrt.grid(row=7,column=3)
########HOVERING SETTINGS#########
Button_list = [B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,Bdot]
Operations = [Bdivide,Bmultiply,Bsub,Bplus,C,Bbackspace,Bparenthesis1,Bparenthesis2,Bsqrt,Bpow,Bpowtwo]
for item in range(len(Button_list)):
    Hover(Button_list[item], '#3F3F3F', '#212121')
for item in range(len(Operations)):
    Hover(Operations[item], '#3F3F3F', '#313131')
Hover(Bequal, '#EF6423', '#ff590C')


###############PROGRAMMER MODE###############
#Frame for Programmer Mode
P_Number =  Frame(root,bg='#515151')
Top_P_Number = Frame(P_Number,bg='#515151')
Bot_P_Number = Frame(P_Number,bg='#515151')

#Functions of various buttons for Programmer Mode
def P_press(num):
    global expression
    expression += str(num)
    value1.set(expression)


#Bin() , hex() and oct() give us the result in form 0oxxx , or 0bxxxxx for exemple,
#we need only the xx which is the number without the numeral system indication, that's why we use slicing [2:], letting out the 2 first digit.
def ToBin(value):
    global expression2
    expression2 = int(bin(int(value))[2:])

def ToHex(value):
    global expression2
#The total is not converted to Integer here as hexa might contain letter from A to F.
    expression2  = hex(int(value))[2:]

def ToOctal(value):
    global expression2
    expression2 = int(oct(int(value))[2:])
    
def P_equal():
    global expression
    global expression2
    #Retriving from the comboBox
    Type2 = Combo2.get()
    if Type2 == "Octal":
        ToOctal(expression)
    elif Type2 == "Hexadecimal":
        ToHex(expression)
    elif Type2 == "Binary":
        ToBin(expression)
    value2.set(expression2)

#Setting for nice aligned grid
for i in range(6):
    Bot_P_Number.grid_rowconfigure(i, pad=1)

for i in range(4):
    Bot_P_Number.grid_columnconfigure(i, pad=1)

###########CONTENT###########
Numeral_systems = ['Binary','Octal','Hexadecimal']
Label1 = Label(Top_P_Number,text="Decimal",width=12,fg='#f1f1f1',bg='#515151',font=('Bahnschrift bold', 10 ),anchor='w',justify=LEFT,relief=FLAT)
Label1.grid(row=0,column=0)

Combo2 = ttk.Combobox(Top_P_Number, values=Numeral_systems,width=10,justify=LEFT)
Combo2.grid(row=1,column=0)

value1_Label = Label(Top_P_Number,textvariable=value1,width=10,height=2,fg='#f1f1f1',bg='#515151',anchor='e',justify=RIGHT,font=('Bahnschrift', 15 ),relief=FLAT)
value1_Label.grid(row=0,column=1)
value2_Label = Label(Top_P_Number,textvariable=value2,width=10,height=2,fg='#f1f1f1',bg='#515151',anchor='e',justify=RIGHT,font=('Bahnschrift', 15 ),relief=FLAT)
value2_Label.grid(row=1,column=1)

B0 = Button(Bot_P_Number,text='0', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(0))
B0.grid(row=5,column=1)
B1 = Button(Bot_P_Number,text='1', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(1))
B1.grid(row=4,column=1)
B2 = Button(Bot_P_Number,text='2', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(2))
B2.grid(row=4,column=2)
B3 = Button(Bot_P_Number,text='3', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(3))
B3.grid(row=4,column=3)
B4 = Button(Bot_P_Number,text='4', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(4))
B4.grid(row=3,column=1)
B5 = Button(Bot_P_Number,text='5', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(5))
B5.grid(row=3,column=2)
B6 = Button(Bot_P_Number,text='6', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(6))
B6.grid(row=3,column=3)
B7 = Button(Bot_P_Number,text='7', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(7))
B7.grid(row=2,column=1)
B8 = Button(Bot_P_Number,text='8', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(8))
B8.grid(row=2,column=2)
B9 = Button(Bot_P_Number,text='9', font=('Bahnschrift', 10 ),width=9,height=3,bg='#212121',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=lambda: P_press(9))
B9.grid(row=2,column=3)

P_Bequal = Button(Bot_P_Number,text='=', font=('Bahnschrift', 10 ),width=9,height=3,bg='#ff590C',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=P_equal)
P_Bequal.grid(row=5,column=3)
P_delete =  Button(Bot_P_Number,text='Del', font=('Bahnschrift', 10 ),width=9,height=3,bg='#313131',fg="#f1f1f1",activebackground='#FF590C',relief=FLAT,command=delete)
P_delete.grid(row=5,column=2)

##########Hovering settings##########
Hover(B_Mode, '#ff590C', '#212121')
Hover(P_Mode, '#ff590C', '#212121')

########LAUNCHING#########
root.mainloop()
