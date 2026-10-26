"""Create a scholarship eligibility checker for a college. Students are selected based on
marks, family INCOME, and attendance"""

S_NAME = input("Enter The Student Name : ")
PERCENTAGES = int(input("Enter Your Percentages : "))
INCOME = int(input("Enter Your Family Income : "))
A_PERCENTAGES = int(input("Enter Your Attendance Percentages : "))

print("Name Of Student :", S_NAME)
if PERCENTAGES >= 75:
    if A_PERCENTAGES >= 75 and A_PERCENTAGES <= 100:
        if INCOME <= 400000 and INCOME >= 0:
            print("Eligible")
            if PERCENTAGES >= 90 and PERCENTAGES <= 100:
                print("Full Scholarship")
            else:
                print("You are eligible for partial Scholarship")
        elif INCOME > 400000:
            print("High Family Income")
            print("Not Eligible")

        else:
            print("Invalid Income")
    elif A_PERCENTAGES < 0 or A_PERCENTAGES > 100:
        print("Enter Valid Attendance Percentages")
    else:
        print("Attendance is low!")
elif PERCENTAGES < 0 or PERCENTAGES > 100:
    print("Enter Valid Percentages")

else:
    print("Low Percentages")
    print("Not eligible")
