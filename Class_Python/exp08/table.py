import tkinter as tk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("student_registration.db")
cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age TEXT,
               course TEXT,
               email TEXT
)
               
  """)
conn.commit()
def  register_student():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_age.get()
    email = entry_email.get()

    if name == "" or age == "" or course == "" or email == "":
        messagebox.showerror("Error","All fields are required")
    else:
        cursor.execute("Insert into student (name,age,course,email) VALUE (?,?,?,?)",
                       (name,age,course,email))
        conn.commit()
        messagebox.showinfo("Success", "Student register successfully")
        
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration Form")

tk.Lable(root,text="Student Registration Form")

tk.Label(root,text="Student Registration", font=("Arial",16)).pack(pady=10)
tk.Label(root,text)