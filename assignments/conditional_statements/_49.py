'''
To print result status using match case.
'''

MARKS = int(input("Enter Your Marks: "))

match MARKS:
    case marks if marks >= 45 and marks <= 100:
        print("Pass")
    case marks if marks < 45:
        print("Fail")
    case _ :
        print("Invalid Marks")
