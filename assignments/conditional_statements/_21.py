'''
to find the smallest of three numbers.

'''
NUM1 = int(input("Enter The First Number : "))
NUM2 = int(input("Enter The Second Number : "))
NUM3 = int(input("Enter The Third Number : "))
if NUM1 < NUM2 and NUM1 < NUM3:
    print("The Smallest Number is : ",NUM1)
elif NUM2 < NUM1 and NUM2 <NUM3:
    print("The Smallest NUmber is : ", NUM2)
else:
    print("The Smallest Number is : ", NUM3)
