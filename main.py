import json
from tabulate import tabulate

# Read the student data from a JSON file
with open('database/data.json', 'r') as file:
    data = json.load(file)

# Extract the student details from the JSON data
students = data['students']

# Print the data in a tabular format
table = []
for student in students:
    table.append([student["name"], student["rollno"],student["attendance"]["subjects"][0]["name"]])

print(tabulate(table, headers=["Name", "Roll No","Attendance"], tablefmt="grid"))
