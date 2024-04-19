import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

# create Treeview with 3 columns
table = ttk.Treeview(root, columns=("name", "age", "gender"), show="headings")

# set column headings
table.heading("name", text="Name")
table.heading("age", text="Age")
table.heading("gender", text="Gender")

# add data to the table
table.insert("", "end", values=("John", 30, "Male"))
table.insert("", "end", values=("Mary", 25, "Female"))
table.insert("", "end", values=("Sam", 35, "Male"))

# pack the table
table.pack(expand=True, fill="both")

root.mainloop()
