from tkinter import *
from pages import loginPage
from pages import homePage

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x600")
        self.login()

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        loginPage(self, self.master)

    def home(self):
        for i in self.master.winfo_children():
            i.destroy()
        return homePage(self,self.master)

root = Tk()
app = App(root)
root.mainloop()
