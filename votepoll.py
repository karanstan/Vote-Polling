#voting poll
#import packages

import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox
import re

window = Tk()
window.geometry("1366x768")

#title
tit = Label(window,text="*** Voting system ***",font=("Courier",20,"bold")).place(x=580,y=20)
hr = Frame(window,height=5,width=1315,bg="black")
hr.place(x=20,y=55)
def Signup():
        name_var = tkinter.StringVar()
        email_var = tkinter.StringVar()
        pass_var = tkinter.StringVar()
        repass_var = tkinter.StringVar()
        def verify():

            name = name_var.get()
            email = email_var.get()
            password = pass_var.get()
            repass = repass_var.get()
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if name == "":
               messagebox.showerror("showerror","kindly provide valid user name")
            if re.search(regex,email):
                if password != repass :
                    messagebox.showerror("showerror","Password does not matched")
                    pass_var.set("")
                    repass_var.set("")
                else :
                    messagebox.showinfo("showeinfo","registered successfully")
                    conn = sqlite3.connect('votebank.db')
                    #conn.execute('''CREATE TABLE VOTEBANK 
                                  # ( NAME TEXT NOT NULL,EMAIL TEXT NOT NULL,PASSWORD TEXT NOT NULL);''' )
                    #once the table is created no need to call Create cammand again
                    conn.execute("""INSERT INTO VOTEBANK (NAME,EMAIL,PASSWORD) VALUES (?,?,?)""",(name,email,password))
                    conn.commit()
                    conn.close()
                    name_var.set("")
                    email_var.set("")
                    pass_var.set("")
                    repass_var.set("")
                    
            else :
                print("Invalid mail")
                messagebox.showerror("showerror","Invalid Email")
                email_var.set("")   
            
            
        tit = Label(window,text="New user,Register to Signup!!!",font=("Courier",15,"bold")).place(x=580,y=200)
        hr = Frame(window,height=5,width=1315,bg="black")
        hr.place(x=20,y=240)
        user_name = Label(window,text = "Username",font=("Courier",10)).place(x=580,y=260)
        user_input = Entry(window,textvariable=name_var,width=30).place(x=660,y=260)
        email = Label(window,text = "Email",font=("Courier",10)).place(x=580,y=300)
        email_input = Entry(window,textvariable=email_var,width=30).place(x=660,y=300)
        password = Label(window,text = "Password",font=("Courier",10)).place(x=580,y=340)
        pass_input = Entry(window,textvariable=pass_var,show="*",width=30).place(x=660,y=340)
        repassword = Label(window,text = "Retype Password",font=("Courier",10)).place(x=520,y=380)
        repass_input = Entry(window,textvariable=repass_var,show="*",width=30).place(x=660,y=380)
        verify1 = Button(window,text="Register",command=verify,width=20).place(x=600,y=450)
       
#login
def login():
    name_var1 = tkinter.StringVar()
    pass_var1 = tkinter.StringVar()
   

    def pollPage():
        
        win = Tk()
        win.geometry("1300x400") 
        val = tkinter.StringVar(win)
        def vote1(win):
            valen1 = val.get()
            name = name_var1.get()
            conn = sqlite3.connect('votebank.db')
            conn.execute("""UPDATE VOTEBANK SET VOTE = ? WHERE NAME= ? """,(valen1,name))
            messagebox.showinfo("showeinfo","your vote has been recorded  successfully!!!")
            name_var1.set("")
            pass_var1.set("")
            conn.commit()
            conn.close() 
        ques1 = Label(win,text="Most Famous Car Company",font=("Courier",20,"bold")).place(x=500,y=20)
        o1 = Radiobutton(win,text="Toyota",variable= val,value="Toyoto").place(x=550,y=70)
        o2 = Radiobutton(win,text="Ford",variable= val,value="Ford").place(x=550,y=110)
        o3 = Radiobutton(win,text="BMW",variable= val,value="BMW").place(x=550,y=150)
        Button(win,text="Vote",command=lambda :vote1(win),width=20).place(x=550,y=190)
        Button(win,text="logout",command=win.destroy,width=20).place(x=700,y=190)
        win.mainloop()
    
    def loginverify():

        nameval = name_var1.get()
        passval = pass_var1.get()
        conn = sqlite3.connect('votebank.db')
        ele = conn.execute("""SELECT password,email FROM VOTEBANK WHERE name = ?""",(nameval,))
        ele = ele.fetchall()

        for val in ele :
            if val[0] == passval :
                pollPage()
                break
            else:
                messagebox.showerror("showerror","invalid userid or password")
                break
        
        else:
            messagebox.showerror("showerror","invalid userid or password")
       
        conn.commit()
        conn.close()
    user_name = Label(window,text = "Username",font=("Courier",10)).place(x=580,y=70)
    user_input = Entry(window,textvariable=name_var1,width=30).place(x=660,y=70)
    password = Label(window,text = "Password",font=("Courier",10)).place(x=580,y=110)
    pass_input = Entry(window,textvariable=pass_var1,width=30,show="*").place(x=660,y=110)
   
    login = Button(window,text="login",command=loginverify, width=20).place(x=580,y=150)
    signup = Button(window,text="signup",width=20,command=Signup).place(x=740,y=150)
login()
window.mainloop()