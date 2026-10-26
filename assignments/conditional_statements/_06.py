'''

to compare two numbers and print the greater one

'''
NUM1 = int(input("Enter The First Number : "))

NUM2 = int(input("Enter The Second Number : "))
if NUM1 > NUM2:
    print(NUM1,"Is greater")
elif NUM1 < NUM2:
    print(NUM2,"Is greater")
else:
    print("Same Numbers")
    