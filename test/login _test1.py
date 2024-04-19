import tkinter as tk
from auth import userAuthenticator

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    result = userAuthenticator(username,password)
    # check if username and password are valid
    if result[0]:
        # successful login
        label_result.config(text=result[1] +" Login successful", fg="green")
    else:
        # failed login
        label_result.config(text="Login failed", fg="red")

# create tkinter window
root = tk.Tk()
root.title("Login Page")
root.geometry("700x600")

# create a menu object
menu = tk.Menu(root)
root.config(menu=menu)

# create a frame widget and center it on the window
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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

# run tkinter main loop
root.mainloop()
