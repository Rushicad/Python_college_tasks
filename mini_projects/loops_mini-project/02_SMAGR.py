
'''Process marks for multiple students and generate a class performance summary.'''

students = int(input("Enter Number Of Students: "))

total_marks = 0
count = 0
pass_count = 0
fail_count = 0

for i in range(1, students + 1):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks Out Of 100: "))

    if marks > 100 or marks < 0:
        print("Enter Valid Marks")
    else:
        if marks >= 75:
            print(name, marks, "- A Grade")
        elif marks >= 60:
            print(name, "- B Grade")
        elif marks >= 50:
            print(name,marks,"- C Grade")
        elif marks >= 40:
            print(name,marks, "- D Grade")
        else:
            print(name,marks,"- Fail")
        total_marks = total_marks + marks
        count = count + 1

        if marks >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1
if count > 0:
    avg = total_marks / count
    print("Average Marks Of Class:", round(avg, 2))
else:
    print("No Valid Marks Entered")
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
