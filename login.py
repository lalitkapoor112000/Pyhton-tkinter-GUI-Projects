from tkinter import *

root=Tk()
root.geometry("555x333")
root.minsize(555,333)

def getvals():
    print(f"Username={uservalue.get()}")
    print(f"Password={passvalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{uservalue.get()},{passvalue.get()}\n")

def showvals():
    f=open("records.txt","r")
    for x in f:
        print(f"{x}\n")

def resdata():
    f=open("records.txt","r+")
    f.seek(0)
    f.truncate()
Label(root,text="Welcome to the portal!",font="verdana 24 bold").grid(row=0,column=5,pady=6,padx=50)
f1=Frame(root)
f1.grid(row=1,column=5)
user=Label(f1,text="Username")
user.grid()
password=Label(f1,text="Password")
password.grid()
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(f1,textvariable=uservalue)
passentry=Entry(f1,textvariable=passvalue)
userentry.grid(row=0,column=5)
passentry.grid(row=1,column=5)

Button(f1,text="Submit",command=getvals).grid()
Button(f1,text="Read from Database",command=showvals).grid()
Button(f1,text="Reset Database",command=resdata).grid()

root.mainloop()
