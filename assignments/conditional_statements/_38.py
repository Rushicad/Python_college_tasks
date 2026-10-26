'''
To check whether a student passed all subjects.
'''

SUB1 = int(input("Enter Marks Of First Subject: "))
SUB2 = int(input("Enter Marks Of Second Subject: "))
SUB3 = int(input("Enter Marks Of Third Subject: "))

if SUB1 >= 45 and SUB2 >= 45 and SUB3 >= 45:
    print("Student Has Passed All Subjects")
elif SUB1 < 45 or SUB2 < 45 or SUB3 < 45:
    print("Student Has Failed In At Least One Subject")
else:
    print("Wrong Data Entered")
