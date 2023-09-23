from customtkinter import *
import pyperclip
import customtkinter
from PIL import Image,ImageTk
from tkinter import PhotoImage,Listbox,Scrollbar,messagebox
import random

main=CTk()
main.geometry("400x450+350+150")
main.resizable(False,False)
main.title("Password Generator")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

main.iconbitmap("password.png")
main.iconphoto(False,ImageTk.PhotoImage(Image.open("password.png")))

def sliderevent(value):
    lenLabel.configure(text=int(value))


name=CTkLabel(main,text='Password Generator',font=('Snap ITC',30),fg_color='green',
              height=50,text_color='white')
name.pack(side=TOP,fill=BOTH)

frameMain=CTkFrame(main,height=400,border_color='green',border_width=2,fg_color='#292929')
frameMain.pack(side=BOTTOM,fill=BOTH,padx=10,pady=10)

def themechange():
    global themeVar


    if themeVar=='dark':
        themeButton.configure(image=lightImg)
        themeVar='light'
        customtkinter.set_appearance_mode('light')
        frameMain.configure(fg_color='#b0afae')
        name.configure(text_color='black')
        themeLabel.configure(text_color='black')
        lengthLabel.configure(text_color='black')
        lenLabel.configure(text_color='black')
        generateButton.configure(text_color='black',border_color='black')
        paslabel.configure(fg_color='#878686',text_color='black')
        try:
            name2.configure(text_color='black')
            clearAllButton.configure(text_color='black',border_color='black')
            clearButton.configure(text_color='black',border_color='black')
            copyButton.configure(text_color='black',border_color='black')
        except:
            pass


    elif themeVar=='light':
        themeButton.configure(image=darkImg)
        customtkinter.set_appearance_mode('dark')
        themeVar='dark'
        frameMain.configure(fg_color='#292929')
        name.configure(text_color='white')
        themeLabel.configure(text_color='white')
        lengthLabel.configure(text_color='white')
        lenLabel.configure(text_color='white')
        generateButton.configure(text_color='white',border_color='white')
        paslabel.configure(fg_color='#4e4f52',text_color='white')
        try:
            name2.configure(text_color='white')
            clearAllButton.configure(text_color='white',border_color='white')
            clearButton.configure(text_color='white',border_color='white')
            copyButton.configure(text_color='white',border_color='white')
        except:
            pass
light=Image.open('off.png')
lightImg=CTkImage(light_image=light,size=(50,20))
dark=Image.open('on.png')
darkImg=CTkImage(dark_image=dark,size=(50,20))
themeVar='dark'
themeLabel=CTkLabel(frameMain,text='Dark Theme',text_color='white',font=('Times',22))
themeLabel.place(x=200,y=10)
themeButton=CTkButton(frameMain,text='',width=20,image=darkImg,hover=False,command=themechange,fg_color='transparent')
themeButton.place(x=310,y=10)

lengthLabel=CTkLabel(frameMain,text='Length of Password',text_color='white',font=('Georgia',20))
lengthLabel.place(x=10,y=50)
slider=CTkSlider(frameMain,width=375,progress_color='green',button_color='green',button_hover_color='darkGreen',
                 number_of_steps=10,from_=5,to=15,command=sliderevent)
slider.place(x=2,y=80)

lenLabel=CTkLabel(frameMain,text='10',text_color='white',font=('Times',20,'bold'))
lenLabel.place(x=350,y=50)

radioVar1=StringVar()
radioVar2=StringVar()
radioVar3=StringVar()
count1=0
count2=0
count3=0
def radioEvent1():
    global count1,radio1
    count1=count1+1
    if count1>1:
        radio1.destroy()
        radio1=CTkRadioButton(frameMain,text='Include Numbers',hover_color='darkGreen',fg_color='green',border_color='green',border_width_checked=8,width=30,height=40,font=('Georgia',22),value='1',variable=radioVar1,command=radioEvent1)
        radio1.place(x=30,y=100)
        radio1.deselect()
        count1=0
def radioEvent2():
    global count2,radio2
    count2=count2+1
    if count2>1:
        radio2.destroy()
        radio2=CTkRadioButton(frameMain,text='Include Alphabets',hover_color='darkGreen',border_color='green',border_width_checked=8,fg_color='green',font=('Georgia',22),value='1',variable=radioVar2,command=radioEvent2)
        radio2.place(x=30,y=150)
        radio2.deselect()
        count2=0
def radioEvent3():
    global count3,radio3
    count3=count3+1
    if count3>1:
        radio3.destroy()
        radio3=CTkRadioButton(frameMain,text='Include Symbols',hover_color='darkGreen',border_color='green',border_width_checked=8,fg_color='green',font=('Georgia',22),value='1',variable=radioVar3,command=radioEvent3)
        radio3.place(x=30,y=195)
        radio3.deselect()
        count3=0

    

radio1=CTkRadioButton(frameMain,text='Include Numbers',hover_color='darkGreen',width=30,height=40,border_color='green',border_width_checked=8,
                      fg_color='green',font=('Georgia',22),value='1',variable=radioVar1,command=radioEvent1)
radio1.place(x=30,y=100)
radio2=CTkRadioButton(frameMain,text='Include Alphabets',hover_color='darkGreen',border_color='green',border_width_checked=8,fg_color='green',font=('Georgia',22),value='1',variable=radioVar2,command=radioEvent2)
radio2.place(x=30,y=150)
radio3=CTkRadioButton(frameMain,text='Include Symbols',hover_color='darkGreen',border_color='green',border_width_checked=8,fg_color='green',font=('Georgia',22),value='1',variable=radioVar3,command=radioEvent3)
radio3.place(x=30,y=195)

def generatePassword():
    pwd=[]
    characters=[chr(i) for i in range(65,91)]
    l2=[chr(j) for j in range(97,123)]
    characters.extend(l2)
    symbols=['_','@','?','&','#','$']
    for i in range(9):
        for i in (random.sample(symbols,1)):
            symbols.append(i)
    num=[str(i) for i in range(0,10)]
    for i in range(5):
        for i in (random.sample(num,1)):
            num.append(i)

    length=int(lenLabel.cget('text'))

    if (radioVar1.get()=='1'):
        if radioVar2.get()=='1' and radioVar3.get()=='1':
            num.extend(characters)
            num.extend(symbols)
            pwd=random.sample(num,length)
        elif radioVar2.get()=='1':
            num.extend(characters)
            pwd=random.sample(num,length)
        elif radioVar3.get()=='1':
            num.extend(symbols)
            pwd=random.sample(num,length)
        else:
            pwd=random.sample(num,length)

    elif radioVar2.get()=='1':
        if radioVar3.get()=='1':
            characters.extend(symbols)
            pwd=random.sample(characters,length)
        else:
            pwd=random.sample(characters,length)

    elif radioVar3.get()=='1':
        pwd=random.sample(symbols,length)

    else:
        messagebox.showerror('Error','Please Select atleast one option')
        return
    finalPwd=''.join(pwd)
    paslabel.configure(text=finalPwd)
    
    with open('pwd.txt','a') as f:
        f.write(finalPwd+'\n')


generateButton=CTkButton(frameMain,text='Generate Password',border_color='white',border_width=1,height=40,font=('Times',25),fg_color='green',hover_color='darkGreen',command=generatePassword)
generateButton.place(x=160,y=240)

paslabel=CTkLabel(frameMain,text='',font=('Times',23),width=300,fg_color='#4e4f52',text_color='white',corner_radius=5)
paslabel.place(x=20,y=310)

def copyPwd():
    pwd=paslabel.cget('text')
    pyperclip.copy(pwd)
    if pwd=='':
        pass
    else:
        messagebox.showinfo('Message','Password Copied')
copydark=Image.open('copy.png')
copylight=Image.open('copy (1).png')
copyImg=CTkImage(dark_image=copylight,light_image=copydark)
copyButton=CTkButton(frameMain,text='',height=20,width=10,border_width=1,fg_color='green',image=copyImg,hover_color='darkGreen',command=copyPwd)
copyButton.place(x=325,y=310)

def clearpwd():
    global pwd_list
    pwd=str(listbox.get(ANCHOR))
    if pwd in pwd_list:
        pwd_list.remove(pwd)
        with open("pwd.txt","w") as f:
            for pwds in pwd_list:
                f.write(pwds+'\n')
        listbox.delete(ANCHOR)

def copypwdhistory():
    pwd=str(listbox.get(ANCHOR))
    pyperclip.copy(pwd)

def clearallpwds():
    global pwd_list
    pwd_list.clear()
    file=open("pwd.txt","w")
    file.close()
    listbox.delete(0,END)

pwd_list=[]
def historyfunc():
    global listbox,name2,copyButton,clearAllButton,clearButton
    new=CTk()
    new.title('History')
    new.geometry('340x400')
    new.resizable(False,False)
    name2=CTkLabel(new,text='HISTORY',font=('Snap ITC',30),fg_color='green',
              height=50,text_color='white')
    name2.pack(side=TOP,fill=BOTH)

    listbox=Listbox(new,width=58,height=16,bg="#2a2c2e",justify='left',cursor='hand2',font=('Times',10),
                fg="white",selectbackground="green",border=3,borderwidth=4)
    listbox.pack(side=LEFT,fill=BOTH, padx=(13,15),pady=(20,50))

    scroll=Scrollbar(listbox,highlightcolor="darkGreen",width=12)
    scroll.pack(side=RIGHT,fill=BOTH,pady=(0,0),padx=(290,0))

    listbox.config(yscrollcommand=scroll.set)
    scroll.config(command=listbox.yview)

    copyButton=CTkButton(new,text='COPY',border_color='white',border_width=1,height=30,width=90,
                         font=('Times',15,'bold'),fg_color='green',hover_color='darkGreen',command=copypwdhistory)
    copyButton.place(x=15,y=360)

    clearButton=CTkButton(new,text='CLEAR',border_color='white',border_width=1,height=30,width=90,
                         font=('Times',15,'bold'),fg_color='green',hover_color='darkGreen',command=clearpwd)
    clearButton.place(x=115,y=360)

    clearAllButton=CTkButton(new,text='CLEAR ALL',border_color='white',border_width=1,height=30,width=90,
                         font=('Times',15,'bold'),fg_color='green',hover_color='darkGreen',command=clearallpwds)
    clearAllButton.place(x=215,y=360)

    try:
        global pwd_list
        with open("pwd.txt","r") as f:
            pwds=f.read()
            pwd=pwds.split('\n')
            for i in pwd:
                if i=='':
                    pwd.remove(i)
            pwd_list=pwd
            for i in pwd_list:
                listbox.insert(END,i.strip())
    except FileNotFoundError:
        file=open("tasklist.txt","w")
        file.close()
    
    new.mainloop()

historydark=Image.open('history.png')
historylight=Image.open('history (1).png')
historyImg=CTkImage(dark_image=historylight,light_image=historydark)
histButton=CTkButton(frameMain,text='',command=historyfunc,height=15,border_width=1,width=15,corner_radius=5,image=historyImg,fg_color='green',hover_color='darkGreen')
histButton.place(x=20,y=345)


main.mainloop()