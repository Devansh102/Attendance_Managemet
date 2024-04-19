from tkinter import *
import loginPage
import homePage


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x600")
        self.master.title("Attendance Portal")
        self.login()

    def navBar(self,usr):
        frame = Frame(self.master)
        frame.pack(side="top", fill="x")
        logo = Label(frame, text="Attendance Management", font=("Arial", 24))
        logo.pack(side="top", fill="x")

        attendance_btn = Button(frame, text="Log Out", command=self.logOut)
        attendance_btn.pack(side="right")

        btn = Button(frame, text="Home", command=lambda:self.homePage(usr))
        btn.pack(side="left")

    def logOut(self):
        # change usr
        self.login()

    # function to change PageState

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        return loginPage.login_page(self)
    
    def homePage(self,usr):
        print(usr.user)
        return self.home(usr)

    def home(self,usr):
        for i in self.master.winfo_children():
            i.destroy()
        self.navBar(usr)
        # self.fr
        # self.attendance_btn = Button(self.frame2, text="Log Out", command=self.logOut)
        # self.attendance_btn.pack()
        homePage.homePageButtons(self,usr)
        # return homePage(self, self.master)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
