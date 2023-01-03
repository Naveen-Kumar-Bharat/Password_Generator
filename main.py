from tkinter import *
from random import randint
import random

root = Tk()
root.title('Password Generator')
root.geometry("500x300")
root.configure(bg="light blue")


def new_rand():
    pass_entry1.delete(0,END)
    pass_length=int(pass_entry.get())

    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    special_characters="!@#$%^&*()"

    upper=True
    lower=True
    nums=True
    spec_char=True

    password=""

    if upper:
        password+=uppercase
    if lower:
        password+=lowercase
    if nums:
        password+=numbers
    if spec_char:
        password+=special_characters
    
    password="".join(random.sample(password,pass_length))   
    pass_entry1.insert(0,password)

def clipper():
    pass

lf=LabelFrame(root,text="Number of Characters",bg="white")
lf.pack(pady=20)

pass_entry=Entry(lf,text='',font=("Times",18))
pass_entry.pack(pady=20,padx=20)

pass_entry1=Entry(root,text='',font=("Times",24,"bold"))
pass_entry1.pack(pady=20)

pass_frame=Frame(root)
pass_frame.pack(pady=10)


pass_button=Button(pass_frame,text="Generate Password",command=new_rand)
pass_button.grid(row=0,column=0,padx=5)

clip_button=Button(pass_frame,text="Copy Password",command=clipper)
clip_button.grid(row=0,column=1,padx=0)

root.mainloop()
