'''
a program to check exam results (Distinction, First Class, Pass, Fail).

'''
MARKS = int(input("Enter Your Marks : "))
if MARKS >= 90 and MARKS <= 100:
    print("Congratulations! You have passed with Distinction")
elif MARKS >= 80 and MARKS <= 89:
    print("Congratulations! You have passed with First Class.")
elif MARKS >= 45 and MARKS <= 79:
    print("Congratulations! You Are Pass.")
elif MARKS <= 44:
    print("You Are Fail!!")
else: 
    print("Invalid Marks")
