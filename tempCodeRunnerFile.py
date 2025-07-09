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
    