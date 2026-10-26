'''
to print menu-based food selection using match case.
'''
print("1. Gulab Jamun")
print("2. Biryani")
print("3. Rice Plate")
print("4. Vadapav")

CHOICE = int(input("Enter The Food Number : "))
match CHOICE:
    case 1:
        print("Gulab Jamun")
    case 2:
        print("Biryani")
    case 3:
        print("Rice Plate")
    case 4:
        print("Vadapav")
    case _:
        print("Invalid Choice")
        