import time
import random
from customtkinter import *
import customtkinter
from PIL import Image,ImageTk
from tqdm import tqdm
from tkinter import messagebox
main=CTk()
 
main.geometry("800x600+200+50")
main.resizable(False,False)
main.title("Rock Paper Scissor")
customtkinter.set_appearance_mode('light')


img=Image.open('bg.jpg')
bgFrameImg=CTkImage(light_image=img,size=(800,600))
bgFrame=CTkFrame(main,width=800,height=600)
bgFrame.pack(side=TOP,fill=BOTH,padx=0,pady=0)
bgLabel=CTkLabel(bgFrame,text="",width=800,height=600,image=bgFrameImg)
bgLabel.pack()

title_label=CTkLabel(main,text='Rock Paper Scissor',width=800,height=70,font=('Bauhaus 93',65),fg_color='brown',text_color='white')
title_label.place(x=-1,y=-1)
frameMain=CTkFrame(main,width=730,height=500,border_width=2,border_color='brown',fg_color='#d9b568')
frameMain.place(x=34,y=85)

choiceLabel=CTkLabel(frameMain,text='Your Choice',width=200,height=30,fg_color='brown',
                     corner_radius=10,text_color='white',font=('Times',40))
choiceLabel.place(x=270,y=20)

radioVar=StringVar()

r1=CTkRadioButton(frameMain,text="Rock",variable=radioVar,value='r',font=('Times',30),text_color='black',fg_color='brown',
                  radiobutton_height=30,radiobutton_width=30,border_color='brown',border_width_checked=10,hover_color='#de8e43')
r1.place(x=100,y=80)
r2=CTkRadioButton(frameMain,text="Paper",variable=radioVar,value='p',font=('Times',30),text_color='black',fg_color='brown',
                  radiobutton_height=30,radiobutton_width=30,border_color='brown',border_width_checked=10,hover_color='#de8e43')
r2.place(x=100,y=130)
r3=CTkRadioButton(frameMain,text="Scissor",variable=radioVar,value='s',font=('Times',30),text_color='black',fg_color='brown',
                  radiobutton_height=30,radiobutton_width=30,border_color='brown',border_width_checked=10,hover_color='#de8e43')
r3.place(x=100,y=180)

game=Image.open("rock-paper-scissors.png")
gameImg=CTkImage(light_image=game,size=(150,150))
mainButton=CTkButton(frameMain,text="",image=gameImg,width=5,hover=False,fg_color='transparent')
mainButton.place(x=500,y=70)



rock=Image.open("fist.png")
rockImg=CTkImage(light_image=rock,size=(35,35))
paper=Image.open("hand-paper.png")
paperImg=CTkImage(light_image=paper,size=(35,35))
scissor=Image.open("scissors.png")
scissorImg=CTkImage(light_image=scissor,size=(40,40))

rockLabel=CTkLabel(frameMain,text="",image=rockImg)
rockLabel.place(x=260,y=80)
paperLabel=CTkLabel(frameMain,text="",image=paperImg)
paperLabel.place(x=260,y=130)
scissorLabel=CTkLabel(frameMain,text="",image=scissorImg)
scissorLabel.place(x=260,y=175)

def restart():
    global generateButton
    if opt=="r":
        r1.deselect()
    elif opt=="p":
        r2.deselect()
    elif opt=="s":
        r3.deselect()
    comLabel.destroy()
    resLabel.destroy()
    winLabel.destroy()
    noButton.destroy()
    youButton.destroy()
    youLabel.destroy()
    reButton.destroy()
    generateButton=CTkButton(frameMain,text='PLAY',corner_radius=10,border_color='brown',command=play,text_color='brown',border_width=3,height=40,font=('Times',25,'bold'),fg_color='#e3ad7b',hover_color='#ed9039')
    generateButton.place(x=320,y=220)

def result():
    global resLabel,winLabel,reButton
    calcLabel.destroy()
    resLabel=CTkLabel(frame2,width=40,text="Result: ",font=('Times',34),text_color='brown',corner_radius=5)
    resLabel.place(x=33,y=113)
    
    winLabel=CTkLabel(frame2,text='',width=200,height=30,fg_color='brown',
                        corner_radius=10,text_color='white',font=('Times',35))
    winLabel.place(x=140,y=115)
    
    if win==True:
        winLabel.configure(text="Congratulations! You won.")
    elif win==False:
        winLabel.configure(text="You Lost! Better Luck Next Time")
    elif win==None:
        winLabel.configure(text="The game is tie!")
        
    reButton=CTkButton(frameMain,text='PLAY AGAIN',corner_radius=10,border_color='brown',command=restart,text_color='brown',border_width=3,height=40,font=('Times',25,'bold'),fg_color='#e3ad7b',hover_color='#ed9039')
    reButton.place(x=320,y=220)

def update():

    global calcLabel,noButton,youButton,youLabel
    comLabel.configure(text=f"Computer chose: {comnew}")
    noButton=CTkButton(frame2,text="",image=comImg,width=5,hover=False,fg_color='transparent')
    noButton.place(x=300,y=15)

    if opt=="r":
        you=opt.replace("r","ROCK")
        youImg=rockImg
    elif opt=="p":
        you=opt.replace("p","PAPER")
        youImg=paperImg
    elif opt=="s":
        you=opt.replace("s","SCISSOR")
        youImg=scissorImg
    youLabel=CTkLabel(frame2,text=f"You chose: {you}",font=('Times',25))
    youLabel.place(x=20,y=60)
    
    youButton=CTkButton(frame2,text="",image=youImg,width=5,hover=False,fg_color='transparent')
    youButton.place(x=250,y=55)

    
    calcLabel=CTkLabel(frame2,text="Calculating Results......",font=('Times',25))
    calcLabel.place(x=20,y=100)

    calcLabel.after(1500,func=result)

def play():
    global comnew,comLabel,opt,win
    opt=radioVar.get()
    ran=random.randint(1,3)
    if ran==1:
        comp="r"
    elif ran==2:
        comp="p"
    elif ran==3:
        comp="s"
    win=False
    if comp==opt:
        win=None
    elif comp=="r":
        if opt=="p":
            win=True
        elif opt=="s":
            win=False
        else:
            win="uk"
    elif comp=="p":
        if opt=="s":
            win=True
        elif opt=="r":
            win=False
        else:
            win="uk"
    elif comp=="s":
        if opt=="r":
            win=True
        elif opt=="p":
            win=False
        else:
            win="uk"

    if win=='uk':
        messagebox.showerror('Error','Please Select atleast one option!')
        return
    
    comnew=""
    global comImg
    if comp=="r":
        comnew=comp.replace("r","ROCK")
        comImg=rockImg
    elif comp=="p":
        comnew=comp.replace("p","PAPER")
        comImg=paperImg
    elif comp=="s":
        comnew=comp.replace("s","SCISSOR")
        comImg=scissorImg

    comLabel=CTkLabel(frame2,text="Computer is choosing: ........ ",font=('Times',25))
    comLabel.place(x=20,y=20)
    generateButton.destroy()
    comLabel.after(1500,func=update)


generateButton=CTkButton(frameMain,text='PLAY',corner_radius=10,border_color='brown',command=play,text_color='brown',border_width=3,height=40,font=('Times',25,'bold'),fg_color='#e3ad7b',hover_color='#ed9039')
generateButton.place(x=320,y=220)
frame2=CTkFrame(frameMain,width=660,height=200,fg_color='#edd077',border_color='brown',border_width=2)
frame2.place(x=30,y=280 )

main.mainloop()

