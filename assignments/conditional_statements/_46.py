'''
To print grade description using match case.
'''

MARKS = int(input("Enter Your Marks: "))

match MARKS:
    case marks if 80 <= marks <= 100:
        print("A Grade")
    case marks if 60 <= marks < 80:
        print("B Grade")
    case marks if 40 <= marks < 60:
        print("C Grade")
    case marks if 0 <= marks < 40:
        print("Fail!!")
    case _:
        print("Invalid Marks")
