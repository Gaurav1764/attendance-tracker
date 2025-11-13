# -------------------------------------------------------------
# Name: GAURAV KUMAR
# Date: 12-Nov-2025
# Roll no.: 2501940033
# Assignment Title: Attendance Tracker - Assignment 01
# Course: Programming for Problem Solving Using Python (ETCCPP171)
# -------------------------------------------------------------

from datetime import datetime

print("Welcome to Attendance Tracker")
print("This program helps you record attendance quickly.\n")

attendance = {}

try:
    n = int(input("How many students to record today? "))

    for i in range(n):
        print("\nEntry", i + 1)
        while True:
            name = input("Enter student name: ").strip()
            if name == "":
                print("Name cannot be empty. Try again.")
                continue
            if name in attendance:
                print("This student is already recorded. Try another.")
                continue
            break

        while True:
            check_in = input("Enter check-in time (HH:MM): ").strip()
            if check_in == "":
                print("Time cannot be empty. Try again.")
                continue
            break

        attendance[name] = check_in

except ValueError:
    print("Invalid number entered.")

print("\n---------- Attendance Summary ----------")
print("Student Name\t\tCheck-in Time")
print("----------------------------------------")

for student, time in attendance.items():
    print(f"{student:20}\t{time}")

print("----------------------------------------")
print("Total Students Present:", len(attendance))

choice = input("\nDo you want to calculate absentees (yes/no)? ").lower()
if choice == "yes":
    try:
        total = int(input("Enter total number of students: "))
        absents = total - len(attendance)
        if absents < 0:
            absents = 0
        print("Total Present:", len(attendance))
        print("Total Absent:", absents)
    except ValueError:
        print("Invalid number entered.")

save = input("\nSave attendance to file (yes/no)? ").lower()
if save == "yes":
    filename = "attendance_log.txt"
    with open(filename, "w") as f:
        f.write("Attendance Report\n")
        f.write("Generated on: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n\n")
        f.write("Student Name\t\tCheck-in Time\n")
        f.write("----------------------------------------\n")
        for student, time in attendance.items():
            f.write(f"{student:20}\t{time}\n")
        f.write("----------------------------------------\n")
        f.write("Total Present: " + str(len(attendance)) + "\n")
        if 'total' in locals():
            f.write("Total Absent: " + str(absents) + "\n")
    print("Attendance saved to", filename)

print("\nAttendance recording complete. Thank you!\n")
