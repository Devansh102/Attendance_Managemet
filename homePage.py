import tkinter as tk
import markAttendancePage
import viewAttendance
import json
x =10
y = 10
def MarkAttendance(self,usr,frame):
    for i in frame.master.winfo_children():
        i.destroy()
    self.navBar(usr)
    markAttendancePage.markAttendance_Page(self,usr,frame)
    return

def ReviewAttendance(self,usr,frame):
    for i in frame.master.winfo_children():
        i.destroy()
    self.navBar(usr)
    viewAttendance.viewAttendance(self,usr,frame)
    return

def viewProfile(self,usr,frame):
        for i in frame.master.winfo_children():
            i.destroy()
        self.navBar(usr)
        professor = {
        "name": "Dr. John Smith",
        "degree": "PhD in Computer Science",
        "contact": {
            "email": "john.smith@university.edu",
            "phone": "+1 (555) 123-4567"
        },
        "department": "Computer Science",
        "office": {
            "building": "Engineering Building",
            "room": "E256"
        },
        "courses": [
            {
            "name": "Introduction to Computer Science",
            "code": "CS101"
            },
            {
            "name": "Data Structures and Algorithms",
            "code": "CS201"
            },
            {
            "name": "Database Systems",
            "code": "CS301"
            }
        ]
        }
        # Professor Name and Department
        frame = tk.Frame(self.master)
        frame.pack()
        name_label = tk.Label(frame, text=professor["name"], font=("Arial", 20, "bold"))
        name_label.pack()
        degree_label = tk.Label(frame, text=professor["degree"], font=("Arial", 12))
        degree_label.pack()
        department_label = tk.Label(frame, text=professor["department"], font=("Arial", 12))
        department_label.pack()
        
        # Professor Contact Info
        contact_label = tk.Label(frame, text="Contact Information", font=("Arial", 14, "bold"))
        contact_label.pack(pady=(20, 10))
        email_label = tk.Label(frame, text=f"Email: {professor['contact']['email']}", font=("Arial", 12))
        email_label.pack()
        phone_label = tk.Label(frame, text=f"Phone: {professor['contact']['phone']}", font=("Arial", 12))
        phone_label.pack()
        
        # Professor Office Info
        office_label = tk.Label(frame, text="Office Information", font=("Arial", 14, "bold"))
        office_label.pack(pady=(20, 10))
        building_label = tk.Label(frame, text=f"Building: {professor['office']['building']}", font=("Arial", 12))
        building_label.pack()
        room_label = tk.Label(frame, text=f"Room: {professor['office']['room']}", font=("Arial", 12))
        room_label.pack()
        
        # Professor Course Info
        courses_label = tk.Label(frame, text="Courses Taught", font=("Arial", 14, "bold"))
        courses_label.pack(pady=(20, 10))
        for course in professor["courses"]:
            course_label = tk.Label(frame, text=f"{course['name']} ({course['code']})", font=("Arial", 12))
            course_label.pack()
        return frame

def display_complaints(self,usr,frame):
    # Create a new window

    with open("database/complaints.json", "r") as f:
        data = json.load(f)
    data = data["complaints"]

    listbox = tk.Listbox(self.master)
    listbox.pack(expand=True, fill='both')
        
        # Add the complaints to the listbox
    for complaint in data:
        text = f"{complaint['name']} - {complaint['date']}: {complaint['complaint']}"
        listbox.insert(tk.END, text)
    return listbox

def showResult(self,usr,frame):
    exam1 = "T1"
    exam2 = "T2"
    for i in frame.master.winfo_children():
        i.destroy()
    self.navBar(usr)
    frame = tk.Frame(self.master)

    # Create a label to display the exam results
    results_label = tk.Label(frame, text="Exam Results", font=("Helvetica", 16, "bold"))
    results_label.place()

    # Create labels and display the exam results for each subject
    exam1_results = [10,10,14,14,12]
    exam2_results = [15,20,14,18,18]
    tk.Label(frame, text="Subject").grid(row=0, column=0)
    tk.Label(frame, text="Exam 1").grid(row=0, column=1)
    tk.Label(frame, text="Exam 2").grid(row=0, column=2)

    # Create table rows for each subject
    for i, subject in enumerate(["Maths", "Science", "English", "History", "Geography"]):
        tk.Label(frame, text=subject).grid(row=i+1, column=0)
        tk.Label(frame, text=exam1_results[i]).grid(row=i+1, column=1)
        tk.Label(frame, text=exam2_results[i]).grid(row=i+1, column=2)

    return frame
    # subject_totals = [sum(scores) for scores in zip(exam1, exam2)]

    # # Create a label for each subject and display the scores for both exams
    # subjects = ["Math", "Science", "English", "History", "Geography"]
    # for i, subject in enumerate(subjects):
    #     label = tk.Label(root, text=f"{subject}: {exam1[i]} ({exam2[i]})", font=("Helvetica", 12, "bold"))
    #     label.grid(row=i, column=0, padx=10, pady=10)

    # # Create labels to display the total scores for each exam and subject
    # exam1_total_label = tk.Label(root, text=f"Exam 1 Total: {exam1_total}", font=("Helvetica", 12, "bold"))
    # exam1_total_label.grid(row=len(subjects), column=0, padx=10, pady=10)

    # exam2_total_label = tk.Label(root, text=f"Exam 2 Total: {exam2_total}", font=("Helvetica", 12, "bold"))
    # exam2_total_label.grid(row=len(subjects)+1, column=0, padx=10, pady=10)

    # for i, subject in enumerate(subjects):
    #     subject_total_label = tk.Label(root, text=f"{subject} Total: {subject_totals[i]}", font=("Helvetica", 12, "bold"))
    #     subject_total_label.grid(row=i, column=1, padx=10, pady=10)





def showButton(self,usr,frame,control,cmd):
        global x
        global y
        button_name = control
        button_name = tk.Button(frame, text=button_name,font=("Arial", 20, "bold"), command=lambda:cmd(self,usr,frame),width=20)
        # button_name.grid(row=x, column=y)
        button_name.pack(pady=10)
        y=+100

def userButtons(self,frame,usr):
    teacher_control = {"Mark Attendance" : MarkAttendance, "Review Attendance" : ReviewAttendance, "View Issues" : display_complaints, "View Profile":viewProfile}
    student_control = {"View Attendance" : ReviewAttendance, "Raise Issue" : " ", "Exam Marks" : showResult,  "View Profile":""}

    if(usr.user == "teacher"):
        i=0
        for control in teacher_control:
            i=+1
            showButton(self,usr,frame,control,teacher_control[control])
    else:
        i=0
        for control in student_control:
            i=+1
            showButton(self,usr,frame,control,student_control[control])



def homePageButtons(self,usr):
    # create a tkinter frame
    frame = tk.Frame(self.master)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    userButtons(self,frame,usr)

    # create buttons for each function and add them to the frame
    # button1 = tk.Button(frame, text="Function 1", command=function1)
    # button1.pack(side=tk.LEFT, padx=10)

    # button2 = tk.Button(frame, text="Function 2", command=function2)
    # button2.pack(side=tk.LEFT, padx=10)

    # button3 = tk.Button(frame, text="Function 3", command=function3)
    # button3.pack(side=tk.LEFT, padx=10)

    # return the frame
    return frame
