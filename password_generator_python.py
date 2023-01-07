# Python program to generate random 
# password using Tkinter module
#import libraries
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
import string,random,pyperclip
from cryptography.fernet import Fernet
import tkinter as tk
import os
import pickle

# create GUI window
win = tk.Tk()#initialized tkinter which creates window
win.geometry('600x500')#set the width and height of window
win.resizable(0,0)#set the fixed size of the window
win.config(bg='ghost white')#set the background colour
win.title("Password Generator Application")#set the title of the window
#win.configure(bg='black')
win['background']='#C0C0C0'

Label(win,text='Password Generator',font ='arial 20 bold' ,bg='#00FFFF').pack()#create label named password generator, set the font and colour of the label
Label(win,text='Created by Fusion Girl',font='arial 15 bold' ,bg='#00FFFF' , width='28').pack(side='bottom')#create label named created by fusion girl, set the colour as 'white smoke' and text as arial,size 15(bold) and 

# declaring a variable of integer type which will be used to store the length of the password entered by the user
pass_len = IntVar()#stores the length of password

# declaring a variable of string type awhich will be used to store the password generated
pass_str = StringVar()#stores generated password
title_password = StringVar()#stores use of password
pass_dec = StringVar()



# Function for generation of password 
def generated_password():
    show_entry.delete(0,tk.END)
    file_entry.delete(0,tk.END)
    e1.delete(0,tk.END)
    e1.insert(0,"Enter file name to save password")
    length = int(pass_len.get())
    generate_password = ""
    if length>=8:
        chars = string.ascii_letters + string.digits + string.punctuation
        for y in range(pass_len.get()):
            generate_password += random.choice(chars)
            pass_str.set(generate_password)
    else:
         show_entry.insert(0,"Minimum Password length must be 8")
# Function for copying password to clipboard

def copy_password():
    pyperclip.copy(pass_str.get())
    show_entry.insert(0,"Password copied")

#encrypting password
key = Fernet.generate_key()
  
# Instance the Fernet class with the key
fernet = Fernet(key)

#save the encrypted password 
def save_password():
    en = fernet.encrypt(pass_str.get().encode())
    f = Fernet(key)
    dirtry = os.getcwd()
    filename = format(dirtry) + "\\"+ title_password.get()
    L = [en,key]
    with open(filename, "wb+") as file:
        pass
        pickle.dump(L,file)
    file.close()
    show_entry.delete(0,tk.END)
    show_entry.insert(0,"Password Encrypted & Saved") 

#decrypting password
def decrypt_password():
    dirtry = os.getcwd()
    filename = format(dirtry) + "\\"+ title_password.get()
    with open(filename, "rb") as file:
        L = pickle.load(file)
        encrypted_message = L[0]
        key = L[1]
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    password = decrypted_message.decode()
    pass_dec.set(password)
    show_entry.delete(0,tk.END)
    show_entry.insert(0,"Password decrypted")

def old_password():
    e1.delete(0,END)
    e1.insert(0,"Enter file name of saved password you want")

def reset_fields():
    gen_entry.delete(0,tk.END)
    file_entry.delete(0,tk.END)
    decry_entry.delete(0,tk.END)
        
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        win.destroy()
        exit()
    
#create label and spinbox for  length of password    
Label(win,text='Set Password Length', font="Times 12 bold",bg='#DDA0DD',fg = "black",width=25,relief=RAISED).place(x=40,y=60)
length = Spinbox(win, from_ = 8, to_ = 32 , textvariable = pass_len , width = 25,bd =3).place(x=300,y=60)

#create button and entry
Button(win, text = "GENERATE PASSWORD" , command = generated_password ,width=25,font='arial 10 bold',bg='#ffb3fe',bd =5).place(x=40,y=100)
gen_entry = Entry(win , textvariable = pass_str,width=30,bd =5)
gen_entry.place(x=300,y=100)#use to create input text field
Button(win,text="Copy to clipboard",command= copy_password,font='arial 10 bold',bg='#ffb3fe' ,bd =5).place(x=250,y=140)
show_entry = Entry(win,width=40,font='arial 10 bold',bg='#C0C0C0')
show_entry.place(x=200,y=180)
file_entry = tk.Entry(win, textvariable = title_password,width=30,bd =5,font='arial 10 bold',bg='#FFF5EE')
file_entry.place(x=360,y=220)     
Button(win, text="SAVE PASSWORD" ,command = save_password,font='arial 10 bold',bg='#ffb3fe' ,bd =5).place(x=250,y=250)
decry_entry=Entry(win , textvariable = pass_dec,width=30,bd =5)
decry_entry.place(x=300,y=300)
Button(win, text = "Decrypt password" , command = decrypt_password ,width=20,font='arial 10 bold',bg='#ffb3fe',bd =5).place(x=40,y=300)
Button(win, text = "Old Password" , command = old_password ,width=20,font='arial 10 bold',bg='#ffb3fe',bd =5).place(x=200,y=350)
Button(win, text = "Reset" , command = reset_fields ,width=5,font='arial 10 bold',bg='#ffb3fe',bd =5).place(x=200,y=400)
Button(win, text = "Exit" , command = Exit,width=5 ,font='arial 10 bold',bg='#ffb3fe',bd =5).place(x=320,y=400)
e1 = Entry(win,width=45,font='arial 10 bold',bg='#DDA0DD')
e1.place(x=10,y=220)
e1.insert(0,"Enter file name to save password")




