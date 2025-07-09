import sqlite3 
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text, charges text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text, gender text, dob text, contact text, admission text, course text, city text, state text, pin text,address text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text ,name text,course text,mark text,full mark text,per text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,fname text ,lname text,contact text,email text, question text,answer text,password text)")
    con.commit()
    
    
    con.close()
create_db()