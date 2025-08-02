from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        title=Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

        
        #========== search ================
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root,text="Search By Roll No.", font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search, font=("goudy old style",20,"bold"),bg="lightyellow").place(x=520,y=100,width=150)
        
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=690,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=35)
                        
        #============Label============
        lbl_roll=Label(self.root,text="Roll No", font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50) 
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Mark Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_fullmarks=Label(self.root,text="Total Mark ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)
        
        self.roll=Label(self.root, font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.Name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.Name.place(x=300,y=280,width=150,height=50) 
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.fullmarks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.fullmarks.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)
        
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=100,height=35)
        
#==============================================


    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                    messagebox.showerror("ERROR","Roll No. should be required.",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None: 
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.Name.config(text=row[2])
                    self.course.config(text=row[3])   
                    self.marks.config(text=row[4])
                    self.fullmarks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.Name.config(text="")
        self.course.config(text="")   
        self.marks.config(text="")
        self.fullmarks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    
    
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student resul first.",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","INVALID student result.",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","result deleted successfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    
    
    
if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()