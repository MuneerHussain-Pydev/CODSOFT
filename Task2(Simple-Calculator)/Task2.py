import math
from customtkinter import *
import customtkinter
from PIL import Image,ImageTk

main=CTk()
main.geometry("300x350+300+150")
main.resizable(False,False)
main.title("Calculator")
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

main.iconbitmap("calculator.png")
main.iconphoto(False,ImageTk.PhotoImage(Image.open("calculator.png")))

def changeTheme():
    global themeVar
    if themeVar=='dark':
        customtkinter.set_appearance_mode('light')
        theme.configure(image=darkImage)
        mainFrame.configure(fg_color='#8e948e')
        themeVar='light'
    elif themeVar=='light':
        customtkinter.set_appearance_mode('dark')
        theme.configure(image=brightImage)
        mainFrame.configure(fg_color="#151716")
        themeVar='dark'

equation=''

def show(Value):
    global equation
    equation+=Value
    inputLabel.configure(text=equation)

def clear():
    global equation
    equation=""
    inputLabel.configure(text=equation)

def backspace():
    global equation
    try:
        equation=equation.removesuffix(equation[-1])
        inputLabel.configure(text=equation)
    except:
        pass

def calculate():
    global equation
    try:
        equation=str(eval(equation))
        inputLabel.configure(text=equation)
    except:
        answer="Error"
        inputLabel.configure(text=answer)
        equation=''

main.bind('<Return>',lambda event:calculate())   
main.bind(1,lambda event:show('1'))   
main.bind(2,lambda event:show('2'))   
main.bind(3,lambda event:show('3'))   
main.bind(4,lambda event:show('4'))   
main.bind(5,lambda event:show('5'))   
main.bind(6,lambda event:show('6'))   
main.bind(7,lambda event:show('7'))   
main.bind(8,lambda event:show('8'))   
main.bind(9,lambda event:show('9'))   
main.bind(0,lambda event:show('0'))   
main.bind('+',lambda event:show('+'))   
main.bind('-',lambda event:show('-'))   
main.bind('*',lambda event:show('*'))   
main.bind('/',lambda event:show('/'))   
main.bind('%',lambda event:show('%'))   
main.bind('.',lambda event:show('.'))   
main.bind('<BackSpace>',lambda event:backspace())   

    


nameLabel=CTkLabel(main,width=120,height=30,text="CALCULATOR",font=('Georgia',20,'bold'),text_color='white',
                   corner_radius=5,fg_color='green')
nameLabel.pack(side=TOP,fill=BOTH,pady=5,padx=(5,48))
themeVar='dark'
darkicon=Image.open('night-mode.png')
darkImage=CTkImage(dark_image=darkicon)
brighticon=Image.open('brightness.png')
brightImage=CTkImage(dark_image=brighticon)
theme=CTkButton(main,text='',font=("Georgia",15,"bold"),image=brightImage,hover=True,corner_radius=5,border_width=0,
          height=30,width=40,fg_color='green',hover_color='lightGreen',command=changeTheme)
theme.place(x=255,y=5)

mainFrame=CTkFrame(main,width=100,height=300,border_width=3,fg_color="#151716",border_color='green')
mainFrame.pack(side=BOTTOM,pady=(0,10),fill=BOTH,padx=5)

inputLabel=CTkLabel(mainFrame,width=300,text="",height=35,fg_color='white',corner_radius=3,text_color='black',font=('Arial',25))
inputLabel.pack(side=TOP,fill=BOTH,padx=(10,10),pady=(10,255))

bC=CTkButton(mainFrame,text='C',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='#073494',
          height=40,width=65,fg_color='#073494',hover_color='#1db5db',command=clear)
bC.place(x=10,y=53)
bM=CTkButton(mainFrame,text='%',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='darkGreen',command=lambda: show('%'))
bM.place(x=80,y=53)
bDivide=CTkButton(mainFrame,text='/',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='darkGreen',command=lambda: show('/'))
bDivide.place(x=150,y=53)
delImg=Image.open('delete.png')
deleteImg=CTkImage(light_image=delImg)
bBack=CTkButton(mainFrame,image=deleteImg,text='',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=60,fg_color='#1d2620',hover_color='#677b80',command=backspace)
bBack.place(x=220,y=53)


b9=CTkButton(mainFrame,text='9',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('9'))
b9.place(x=10,y=100)
b8=CTkButton(mainFrame,text='8',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('8'))
b8.place(x=80,y=100)
b7=CTkButton(mainFrame,text='7',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('7'))
b7.place(x=150,y=100)
bMultiply=CTkButton(mainFrame,text='*',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=60,fg_color='#1d2620',hover_color='darkGreen',command=lambda: show('*'))
bMultiply.place(x=220,y=100)


b6=CTkButton(mainFrame,text='6',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('6'))
b6.place(x=10,y=147)
b5=CTkButton(mainFrame,text='5',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('5'))
b5.place(x=80,y=147)
b4=CTkButton(mainFrame,text='4',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('4'))
b4.place(x=150,y=147)
bPlus=CTkButton(mainFrame,text='+',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=60,fg_color='#1d2620',hover_color='darkGreen',command=lambda: show('+'))
bPlus.place(x=220,y=147)


b3=CTkButton(mainFrame,text='3',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('3'))
b3.place(x=10,y=194)
b2=CTkButton(mainFrame,text='2',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('2'))
b2.place(x=80,y=194)
b1=CTkButton(mainFrame,text='1',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('1'))
b1.place(x=150,y=194)
bMinus=CTkButton(mainFrame,text='-',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=60,fg_color='#1d2620',hover_color='darkGreen',command=lambda: show('-'))
bMinus.place(x=220,y=194)


bPoint=CTkButton(mainFrame,text='.',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('.'))
bPoint.place(x=10,y=241)
b0=CTkButton(mainFrame,text='0',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=65,fg_color='#1d2620',hover_color='#677b80',command=lambda: show('0'))
b0.place(x=80,y=241)
bEqual=CTkButton(mainFrame,text='=',font=("Times",15,"bold"),hover=True,corner_radius=0,border_width=1,border_color='green',
          height=40,width=130,fg_color='green',hover_color='#11c90e',command=calculate)
bEqual.place(x=150,y=241)




main.mainloop()