'''
to check whether a number is divisible by both 3 and 7 or not.

'''
NUM = int(input("Enter The Number : "))
if NUM % 3 == 0 and NUM % 7 == 0:
    print("Number Is Divisible BY Both Numbers")
elif NUM % 3 == 0:
    print("Number is Divisible By 3")
elif NUM % 7 == 0:
    print("Number is Divisible By 7")
else:
    print("Number is not Divisible by Both")
