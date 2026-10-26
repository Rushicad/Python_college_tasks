'''
to check whether a number is positive and even using nested if.

'''
NUM = int(input("Enter The Number : "))
if NUM > 0:
    if NUM % 2 ==0:
        print("The Number Is Positive And Even")
    else:
        print("The Number Is Positive But Not Even")
else:
    print("Negative Number")
