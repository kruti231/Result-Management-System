from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)


        #vaiables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_mark=StringVar()
        self.var_fullmark=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        
        #--------------widgets-------------
        lbl_select=Label(self.root,text="Select Student", font=("goudy old style",15,"bold"),bg="white").place(x=50,y=100)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160) 
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=220)
        lbl_marks=Label(self.root,text="Mark Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=280)
        lbl_fullmarks=Label(self.root,text="Full Mark ",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=340)
        

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=180)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=480,y=100,width=100,height=28)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=160,width=300)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=220,width=300)
        txt_marks=Entry(self.root,textvariable=self.var_mark,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=280,y=280,width=300)
        txt_fullmarks=Entry(self.root,textvariable=self.var_fullmark,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=280,y=340,width=300)
        
        
        #===========================Button===============================
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)

        #========image=========
        self.bg_img=Image.open("image/result.png")
        self.bg_img=self.bg_img.resize((500,300),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)
        
    #===================================================
    
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
            
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None: 
                self.var_name.set(row[0])  
                self.var_course.set(row[1])   
            else:
                messagebox.showerror("Error","No record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record.",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result Already present",parent=self.root)
                else:
                    per=(int(self.var_mark.get())*100)/int(self.var_fullmark.get())
                    cur.execute("insert into result (roll,name,course,mark,fullmark,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_mark.get(),
                        self.var_fullmark.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_mark.set(""),
        self.var_fullmark.set(""),
                        
       
if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()