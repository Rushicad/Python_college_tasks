'''
to check whether a number is divisible by 3 and 5.
'''
NUM = int(input("Enter The Number : "))
if NUM % 3 == 0 and NUM % 5 == 0:
    print("Number Is Divisible By Both 3 and 5")
elif NUM % 3 == 0:
    print("Number Is Only Divisible By 3")
elif NUM % 5 ==0:
    print("Number Is Only Divisible BY 5")
else:
    print("Number Is Not Divisible Anyone")
