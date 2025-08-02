from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox,ttk
import os

class Login_window:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        #============Background Colors=========
        
        self.lbl=Label(self.root,bg="#08A3D2",bd=0)
        self.lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        self.right_lbl=Label(self.root,bg="#031F3c",bd=0)
        self.right_lbl.place(x=0,y=0,relheight=1,width=600)
       
        #===========Frames=========
        loginframe=Frame(self.root,bg="white")
        loginframe.place(x=250,y=100,width=800,height=500)
        title=Label(loginframe,text="Login Here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        Email=Label(loginframe,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_Email=Entry(loginframe,font=("times new roman",15),fg="gray")
        self.txt_Email.place(x=250,y=180,width=350,height=35)
        
        pass_=Label(loginframe,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(loginframe,font=("times new roman",15),fg="gray",show="*")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)
        
        btn_reg=Button(loginframe,text="Register new Account?",font=("times new roman",15,),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=250,y=320)
        btn_gorget=Button(loginframe,text="Forget Password?",font=("times new roman",15,),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.forget_password_window).place(x=450,y=320)
       
        btn_login=Button(loginframe,text="Login",font=("times new roman",20,"bold"),fg="white",bd=0,bg="#B00857",cursor="hand2",command=self.Login).place(x=250,y=360,width=180,height=40)
           
           
           
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_pass_.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_Email.delete(0,END)
        
        
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_pass_.get()=="" or self.txt_Email.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email = ? and question=? and answer=?",(self.txt_Email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the correct security Question /")
            except Exception as es:
                pass
    def forget_password_window(self):
        if self.txt_Email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_Email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
            
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
            #==================== Forget Password============
                    question=Label(self.root2,text="Secutity Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
        
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)
        
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.new_password=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.new_password.place(x=50,y=290,width=250)
        
                    btn_change_pass=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=80,y=340)  
               
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)
            
            
        
        
        
    def register_window(self):
        self.root.destroy()
        os.system("python register.py")
        
    def Login(self):
        if self.txt_Email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("ERROR","All Field are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_Email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome : {self.txt_Email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python Dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("ERROR",f"error due to:{str(es)}",parent=self.root)
                
        
        
if __name__=="__main__":           
    root=Tk()
    obj=Login_window(root)
    root.mainloop()        