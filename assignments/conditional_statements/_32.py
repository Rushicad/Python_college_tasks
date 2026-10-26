'''
To check whether a student is eligible for an exam (attendance + marks)
'''

ATTENDANCE = float(input("Enter Your Attendance In Percentage (%): "))
MARKS = int(input("Enter Your Marks: "))

if ATTENDANCE < 0 or ATTENDANCE > 100 or MARKS < 0 or MARKS > 100:
    print("Invalid Information")
elif ATTENDANCE >= 75 and MARKS >= 80:
    print("You Are Eligible For Exam")
else:
    print("You Are Not Eligible For Exam")
