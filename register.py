from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        self.lbl=Label(self.root,bg="#08A3D2",bd=0)
        self.lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        self.right_lbl=Label(self.root,bg="#031F3c",bd=0)
        self.right_lbl.place(x=0,y=0,relheight=1,width=600)
       
        self.left=ImageTk.PhotoImage(file="image/3.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=300,height=400)
       
        #==========Register frame===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        contact_name=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email_name=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        question_name=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_question['values']=("select","your First pet name","your birth place","your best fiend name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
        
        ans_name=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_ans=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_ans.place(x=370,y=270,width=250)
        
        password_name=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword_name=Label(frame1,text="Confirm password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        
        register_btn = Button(frame1, text="Register", bg="blue", fg="white", font=("Arial", 12, "bold"), cursor="hand2",command=self.register_data)
        register_btn.place(x=50, y=420, width=150, height=40)

        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2",command=self.login_window).place(x=630,y=520,height=40,width=150)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
        
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_ans.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()==""or self.txt_email.get()=="" or self.cmb_question.get()=="select" or self.txt_ans.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("ERROR","Password and Confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("ERROR","Please Agree our terms and condition",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                     messagebox.showerror("ERROR","User already Exist,please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee (fname, lname,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_question.get(),
                                self.txt_ans.get(),
                                self.txt_password.get()  
                                ))
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
            


if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
    