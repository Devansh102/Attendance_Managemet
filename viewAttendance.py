import tkinter as tk
import json

def gohome(self,usr):
    self.home(usr)

def viewAttendance(self,usr,frame):

    with open("database/data.json", "r") as f:
        data = json.load(f)
    students = data["students"]
    student_data = students[0]
    # Create a tkinter window
    frame = tk.Frame(self.master)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    data = student_data

    name_label = tk.Label(frame, text="Student Name: " + data["name"],font=("Arial",20),pady=10)
    name_label.pack()

    # create a label to display student roll number
    rollno_label = tk.Label(frame, text="Roll Number: " + data["rollno"])
    rollno_label.pack()

    # create a label to display attendance for each subject
    attendance_label = tk.Label(frame, text="Attendance:")
    attendance_label.pack()

    for subject in data["attendance"]["subjects"]:
        subject_name_label = tk.Label(frame, text=subject["name"])
        subject_name_label.pack()

        subject_attendance_label = tk.Label(frame, text="Present: " + str(subject["attended_classes"]) + " Absent: " + str(subject["absent_classes"]) + " Percentage: " + subject["percentage"])
        subject_attendance_label.pack()

        # create a table to display marks for each date
        date_label = tk.Label(frame, text="Date")
        date_label.grid(row=3, column=0)

        marking_label = tk.Label(frame, text="Marking")
        marking_label.grid(row=3, column=1)

        for i, date in enumerate(subject["marks"]["date"]):
            date_cell = tk.Label(frame, text=date)
            date_cell.grid(row=i+4, column=0)

            marking_cell = tk.Label(frame, text=subject["marks"]["marking"][i])
            marking_cell.grid(row=i+4, column=1)

        # create a separator between subjects
        separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)
    return frame