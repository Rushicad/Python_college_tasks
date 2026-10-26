'''
to check grade based on marks (A, B, C, Fail).

'''
MARKS = int(input("Enter Your Marks : "))
if MARKS >= 90 and MARKS <= 100:
    print("A Grade")
elif MARKS >= 70 and MARKS <= 89:
    print("B Grade")
elif MARKS >= 45 and MARKS <= 69:
    print("C Grade")
elif MARKS <= 44:
    print("Fail!!")
else: 
    print("Invalid Marks")
