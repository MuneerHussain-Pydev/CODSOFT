from customtkinter import *
import customtkinter
import sqlite3
from PIL import Image,ImageTk
from tkinter import Listbox,Scrollbar,messagebox

def clearTasks():
    task_list.clear()
    file=open("tasklist.txt","w")
    file.close()
    listbox.delete(0,END)
    infoLabel.configure(text='All Tasks have been cleared!')


def addTask():
    task=taskEntry.get()
    taskEntry.delete(0,END)
    if task in task_list:
        box=messagebox.askquestion('DUPLICATE TASK','DO YOU WANT TO ADD '+task+' AGAIN?',icon='warning')
        if box=='yes':
            pass
        else:
            return
    if task:
        with open("tasklist.txt","a") as f:
            f.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
        taskEntry.focus()
        infoLabel.configure(text=task+' has been added!')

def markCompleted():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        if 'COMPLETED!' in task:
            messagebox.showinfo('WARNING','This task has already been Completed')
            infoLabel.configure(text='')
            return
        ind=task_list.index(task)
        task_list.remove(task)
        task_list.insert(ind,task+'        (COMPLETED!)')
        listbox.delete(0,END)
        with open("tasklist.txt","w") as f:
            for tasks in task_list:
                f.write(tasks.strip()+'\n')
                listbox.insert(END, tasks.strip())
        infoLabel.configure(text=task+' has marked as completed')
        
def uncheckTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    print(task)
    if task in task_list:
        if 'COMPLETED!' in task:
            ind=task_list.index(task)
            task_list.remove(task)
            task=task.removesuffix('(COMPLETED!)')
            task_list.insert(ind,task.strip())
            listbox.delete(0,END)
            with open("tasklist.txt","w") as f:
                for tasks in task_list:
                    f.write(tasks.strip()+'\n')
                    listbox.insert(END, tasks.strip())
            infoLabel.configure(text=task.strip()+' has marked as incomplete!')
        else:
            messagebox.showinfo('WARNING','This task is already incomplete!')
            infoLabel.configure(text='')
            return
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as f:
            for tasks in task_list:
                f.write(tasks+'\n')
        listbox.delete(ANCHOR)
        infoLabel.configure(text=task+' has been deleted!')
        
task_list=[]
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as f:
            tasks=f.read()
            task=tasks.split('\n')
            for i in task:
                if i=='':
                    task.remove(i)
            task_list=task
            print(task_list)
            for i in task_list:
                listbox.insert(END,i.strip())
    except FileNotFoundError:
        file=open("tasklist.txt","w")
        file.close()

master=CTk()
master.geometry("650x530")
master.resizable(False,False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
master.title("To-do-list")
master.iconbitmap("sketchbook.png")
master.iconphoto(False,ImageTk.PhotoImage(Image.open("sketchbook.png")))

#topLabel
mainFont=CTkFont(family="Algerian",size=40,weight="bold",slant='roman')
main_label=CTkLabel(master,width=400,height=50,text='To Do List',font=mainFont, fg_color="navyBlue",    
                corner_radius=40,text_color="white")
main_label.place(x=125,y=30)

nImg=Image.open('notepad.png')
noteImg=CTkImage(dark_image=nImg,size=(30,30))
CTkLabel(master,image=noteImg,text=None).place(x=440,y=38)
noteImg=CTkImage(dark_image=nImg,size=(30,30))
CTkLabel(master,image=noteImg,text=None).place(x=180,y=38)


#main
taskFrame=CTkFrame(master,width=500,height=410,corner_radius=10,border_color="black",border_width=3)
taskFrame.place(x=30,y=100)

task=StringVar()
taskEntry=CTkEntry(taskFrame,corner_radius=10,border_color="navyBlue",border_width=2,
                   width=360,placeholder_text="Write a Task",height=35)
taskEntry.place(x=10,y=10)
taskEntry.focus()

listbox=Listbox(taskFrame,width=58,height=16,bg="#2a2c2e",justify='left',cursor='hand2',font=('Times',10),
                fg="white",selectbackground="navyBlue",border=3,borderwidth=4)
listbox.pack(side=LEFT,fill=BOTH, padx=(13,0),pady=(60,15))

scroll=Scrollbar(taskFrame,highlightcolor="navyBlue",width=12)
scroll.pack(side=RIGHT,fill=BOTH,pady=(60,15),padx=(0,15))

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
openTaskFile()

infoLabel=CTkLabel(master,width=580,height=35,text='',font=('Georgia',20), fg_color="navyBlue",    
                corner_radius=40,text_color="white")
infoLabel.place(x=30,y=460)

copyright=CTkLabel(master,text='© All Rights reserved to Muneer Hussain',bg_color='transparent',text_color='white')
copyright.place(x=410,y=505)

#buttons
addimg=Image.open('add.png')
addImage=CTkImage(dark_image=addimg)
CTkButton(master,text="ADD TASK",font=("Georgia",15,"bold"),image=addImage,hover=True,corner_radius=15,border_width=3,
          height=30,border_color="black",fg_color='navyBlue',width=60,hover_color="blue",command=addTask).place(x=450,y=120)

delimg=Image.open('delete.png')
delImage=CTkImage(dark_image=delimg)
CTkButton(master,text="DELETE TASK",font=("Georgia",15,"bold"),image=delImage,hover=True,corner_radius=15,border_width=3,
          height=30,border_color="black",width=60,hover_color="blue",fg_color='navyBlue',command=deleteTask).place(x=450,y=160)

markimg=Image.open('check-mark.png')
markImage=CTkImage(dark_image=markimg)
CTkButton(master,text="MARK AS\nCOMPLETED",font=("Georgia",15,"bold"),image=markImage,hover=True,corner_radius=15,border_width=3,
          height=30,border_color="black",width=60,hover_color="blue",fg_color='navyBlue',command=markCompleted).place(x=450,y=200)

unmarkimg=Image.open('square.png')
unmarkImage=CTkImage(dark_image=unmarkimg)
CTkButton(master,text="UNMARK FROM\nCOMPLETED",font=("Georgia",15,"bold"),image=unmarkImage,hover=True,corner_radius=15,border_width=3,
          height=30,border_color="black",width=60,hover_color="blue",fg_color='navyBlue',command=uncheckTask).place(x=450,y=260)
          
clearimg=Image.open('clear.png')
clearImage=CTkImage(dark_image=clearimg)
CTkButton(master,text="CLEAR ALL \nTASKS",font=("Georgia",15,"bold"),image=clearImage,hover=True,corner_radius=15,border_width=3,
          height=30,border_color="black",width=60,hover_color="blue",fg_color='navyBlue',command=clearTasks).place(x=450,y=320)
          

master.mainloop()