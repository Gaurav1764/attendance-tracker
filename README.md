# attendance-tracker
Attendance Tracker

Author: Gaurav Kumar
Roll No.: 2501940033
Course: MCA (AI/ML)
Faculty: Ms. Neha Kaushik
Assignment Title: Attendance Tracker

Project Overview

The Attendance Tracker is a terminal-based Python application designed to simplify classroom attendance management.
It allows educators to record, verify, and export attendance efficiently — all through a simple and user-friendly command-line interface.

The system provides automatic time stamping, data validation, formatted summaries, absentee calculation, and the option to save or export reports.

Latest Attendance Report (from attendance_log.txt)

Report Generated On: 13-11-2025 17:57:23

No.	Student Name	Check-in Time
1	Gaurav	10:12
2	Shail	10:11
3	SK	09:45
4	Arshit	05:45
5	Aadi	06:45
6	Rahul	09:50
7	Ravi	06:55
8	Neha	07:15
9	Pankaj	06:40
10	Saksham	03:45

Total Present: 10
Total Absent: 5

Sample Program Flow
Step 1 — Adding Student Entries
Enter number of students to record: 10
Student 1 → Gaurav
Student 2 → Shail
Student 3 → SK
...

Step 2 — Viewing Attendance Summary
Attendance Summary
------------------------------------------
Name             Check-in Time
------------------------------------------
Gaurav           10:12
Shail            10:11
SK               09:45
...
------------------------------------------
Total Present: 10

Step 3 — Absentee Calculation
Do you want to calculate absentees? (yes/no): yes
Enter total number of students: 15
Total Present: 10
Total Absent : 5

Step 4 — Report Export
Do you want to save this attendance record? (yes/no): yes
Attendance successfully saved to 'attendance_log.txt'!

Example Report File Content (attendance_log.txt)
Attendance Report
Generated on: 13-11-2025 17:57:23

Student Name        Check-in Time
----------------------------------------
Gaurav              10:12
Shail               10:11
SK                  09:45
Arshit              05:45
Aadi                06:45
Rahul               09:50
Ravi                06:55
Neha                07:15
Pankaj              06:40
Saksham             03:45
----------------------------------------
Total Present: 10
Total Absent: 5
