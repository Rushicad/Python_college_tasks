'''
to check the type of number (single, double, or three digit).

'''
NUM = int(input("Enter The Number : "))
if NUM >= 0 and NUM <= 9:
    print("Single Digit Number")
elif NUM >= 10 and NUM <= 99:
    print("Double Digit Number")
elif NUM >= 100 and NUM <= 999:
    print("Three Digit Number")
else:
    print("Number Is Greater Than Three Digits")
