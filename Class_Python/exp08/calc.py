import tkinter as tk
from tkinter import messagebox

def add():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_lable.config(text="Result "+ str(n1+n2))

def sub():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_lable.config(text="Result "+ str(n1-n2))

def mult():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_lable.config(text="Result "+ str(n1*n2))
def divide():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    if n2==0:
        messagebox.showerror("Error", "Cannot divide by zero")
    else:
        result_lable.config(text="Resut: " + str(n1/n2))

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("450x400")
root.resizable(False,False)

tk.Label(root,text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root,text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Add", width = 10, command=add).pack(pady=5)
tk.Button(root, text="Subtract", width = 10, command=sub).pack(pady=5)
tk.Button(root, text="Multiply", width = 10, command=mult).pack(pady=5)
tk.Button(root, text="Division", width = 10, command=divide).pack(pady=5)

result_lable = tk.Label(root, text="Result: ", font=("Arial",12))
result_lable.pack(pady=10)
root.mainloop()