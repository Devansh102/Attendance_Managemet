import tkinter as tk
from auth import userAuthenticator
from localUser import localUser
import time


def loginSuccess(self, result):
    for i in self.master.winfo_children():
        i.destroy()
    frame = tk.Frame(self.master)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label_result = tk.Label(frame)
    label_result.grid(row=3, column=0, columnspan=2)
    label_result.config(text=result[1] + " Login successful", fg="green")
    return frame
    

def login_page(self):
    # create a frame widget and center it on the window
    frame = tk.Frame(self.master)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label = tk.Label(self.master, text="Login",font=("Arial",20,"bold"),pady=100)
    label.pack()


    def check_login():
        username = entry_username.get()
        password = entry_password.get()
        try:
            result = userAuthenticator(username, password)
            # failed login
            if result is None:
                label_result.config(text="Login failed", fg="red")
            # check if username and password are valid
            elif result[0]:
                # successful login
                # label_result.config(text=result[1] + " Login successful", fg="green")
                usr=localUser(username,password,result[1])
                loginSuccess(self, result)
                self.homePage(usr)
                

        except TypeError as e:
            label_result.config(text="An error occurred: {}".format(e), fg="red")
    
    # logo = tk.Label(frame, text="Attendance Management", font=("Arial", 24))
    # logo.grid(row=1, column=1)

    # create labels for username and password fields
    label_username = tk.Label(frame, text="Username:")
    label_username.grid(row=0, column=0)

    label_password = tk.Label(frame, text="Password:")
    label_password.grid(row=1, column=0)

    # create entry fields for username and password
    entry_username = tk.Entry(frame)
    entry_username.grid(row=0, column=1)

    entry_password = tk.Entry(frame, show="*")
    entry_password.grid(row=1, column=1)

    # create login button
    button_login = tk.Button(frame, text="Login", command=check_login)
    button_login.grid(row=2, column=0, columnspan=2)

    # create label for result message
    label_result = tk.Label(frame)
    label_result.grid(row=3, column=0, columnspan=2)



