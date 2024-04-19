from tkinter import *
import tkinter as tk
import datetime
import json

subject_name = "Maths"
def getUserId(self,usr,frame):
    with open('database/data.json') as f:
        data = json.load(f)
    students = data['students']

    row_frame = tk.Frame(frame)
    row_frame.pack(side="top", fill="x")

# create a label widget for the student name
    name_label = tk.Label(row_frame, text="Name", font=("Arial", 20), padx=26, pady=10,width=10)
    name_label.pack(side="left")

# create a label widget for the student ID
    id_label = tk.Label(row_frame, text="Rolno", font=("Arial", 20), padx=30, pady=10,width=10)
    id_label.pack(side="left")

    attendence_label = tk.Label(row_frame, text="Attendance", font=("Arial", 20), padx=30, pady=10,width=10)
    attendence_label.pack(side="left")

    for student in students:
        makeStudentList(self,frame,student,student['rollno'])

    # create a submit button
    submit_button = tk.Button(frame, text="Submit", command=lambda: submitAttendance(self,usr,students))
    submit_button.pack(side="top", pady=10)

def makeStudentList(self,frame, student, id):
    row_frame = tk.Frame(frame)
    row_frame.pack(side="top", fill="x")

    # create a label widget for the student name
    name_label = tk.Label(row_frame, text=student["name"], font=("Arial", 14), width=20, padx=10, pady=10)
    name_label.pack(side="left")

    # create a label widget for the student ID
    id_label = tk.Label(row_frame, text=id, font=("Arial", 14), padx=10, pady=10,width=20)
    id_label.pack(side="left")

    # create a variable to store the selected attendance
    attendance_var = tk.StringVar()

    # create a radial button for "Present" attendance
    present_button = tk.Radiobutton(row_frame, text="Present", variable=attendance_var, value="P", font=("Arial", 14), padx=10, pady=10)
    present_button.pack(side="left")

    # create a radial button for "Absent" attendance
    absent_button = tk.Radiobutton(row_frame, text="Absent", variable=attendance_var, value="A", font=("Arial", 14), padx=10, pady=10)
    absent_button.pack(side="left")

    # store the attendance variable in the student data
    student["attendance"] = attendance_var

# def makeStudentList(frame,student,id):
#     row_frame = tk.Frame(frame)
#     row_frame.pack(side="top", fill="x")

#     # create a label widget for the student name
#     name_label = tk.Label(row_frame, text=student["name"], font=("Arial", 12),width=20)
#     name_label.pack(side="left", padx=10)

#     # create a label widget for the student ID
#     id_label = tk.Label(row_frame, text=id, font=("Arial", 12))
#     id_label.pack(side="left", padx=10)

#     # create a variable to store the selected attendance
#     attendance_var = tk.StringVar()

#     # create a radial button for "Present" attendance
#     present_button = tk.Radiobutton(row_frame, text="Present", variable=attendance_var, value="P")
#     present_button.pack(side="left", padx=10)

#     # create a radial button for "Absent" attendance
#     absent_button = tk.Radiobutton(row_frame, text="Absent", variable=attendance_var, value="A")
#     absent_button.pack(side="left", padx=10)

#     # store the attendance variable in the student data
#     student["attendance"] = attendance_var

i=0
def attendenceTraverse(attendence):
    i=+1
    return attendence[i-1]

def saveData(self,usr,attendance):
    f = open('database/data.json', 'r+')
    data = json.load(f)
    students = data['students']
    idx=0
    for student in students:
    # Iterate through the subjects for each student
        for subject in student["attendance"]["subjects"]:
        # If the subject is Maths, mark attendance
            if subject["name"] == "Maths":
                subject["marks"]["date"].append(str(datetime.datetime.now()))
                subject["marks"]["marking"].append(attendenceTraverse(attendance))
        idx=idx+1
    f.seek(0)
    json.dump(data, f, indent=4)

    return self.home(usr)


def submitAttendance(self,usr,students):
    # loop through the students and append their attendance to the main data
    for student in students:
        attendance = student["attendance"].get()
    saveData(self,usr,attendance)

    # write the updated data to the file
    # with open('database/data.json', 'w') as f:
    #     json.dump({"students": students}, f)
def markAttendance_Page(self,usr,frame):
    frame = Frame(self.master)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    getUserId(self,usr,frame)
    return frame
