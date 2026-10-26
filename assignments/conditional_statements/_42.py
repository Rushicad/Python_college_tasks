'''
To perform calculator operations using match case
'''

NUM1 = int(input("Enter First Number: "))
NUM2 = int(input("Enter Second Number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

CHOICE = int(input("Enter Your Choice: "))

match CHOICE:
    case 1:
        print("The Addition Of Numbers:", NUM1 + NUM2)
    case 2:
        print("The Subtraction Of Numbers:", NUM1 - NUM2)
    case 3:
        print("The Multiplication Of Numbers:", NUM1 * NUM2)
    case 4:
        if NUM2 == 0:
            print("Cannot Divide By Zero")
        else:
            print("The Division Of Numbers:", NUM1 / NUM2)
    case _:
        print("Invalid Choice")
