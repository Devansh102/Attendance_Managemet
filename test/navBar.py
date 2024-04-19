import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # set window title
        self.title("My App")

        # set window size and center on screen
        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

        # create logo
        logo = tk.Label(self, text="My App Logo", font=("Arial", 24), bg="white")
        logo.pack(side="top", fill="x")

        # create navigation bar
        nav_bar = tk.Frame(self, bg="gray")
        nav_bar.pack(side="top", fill="x")

        # add navigation buttons to the navigation bar
        home_button = ttk.Button(nav_bar, text="Home", command=self.show_home_page)
        home_button.pack(side="left", padx=10)

        about_button = ttk.Button(nav_bar, text="About", command=self.show_about_page)
        about_button.pack(side="left", padx=10)

        contact_button = ttk.Button(nav_bar, text="Contact", command=self.show_contact_page)
        contact_button.pack(side="left", padx=10)

        # create container frame for pages
        self.pages = tk.Frame(self)
        self.pages.pack(expand=True, fill="both")

        # create home page
        self.home_page = tk.Label(self.pages, text="Welcome to the Home Page!", font=("Arial", 20))
        self.home_page.pack(pady=10)

        # create about page
        self.about_page = tk.Label(self.pages, text="This is the About Page.", font=("Arial", 20))
        self.about_page.pack(pady=10)

        # create contact page
        self.contact_page = tk.Label(self.pages, text="Contact us at myapp@example.com", font=("Arial", 20))
        self.contact_page.pack(pady=10)

    def show_home_page(self):
        self.home_page.tkraise()

    def show_about_page(self):
        self.about_page.tkraise()

    def show_contact_page(self):
        self.contact_page.tkraise()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
