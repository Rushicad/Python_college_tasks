'''
to check ticket price based on age

'''
AGE = int(input("Enter Your Age : "))
if AGE <= 10:
    print("Ticket Price is 50rs.")
elif AGE >= 11 and AGE <= 25:
    print("Ticket Price is 70rs")
elif AGE >= 26 and AGE <= 100:
    print("Ticket Price is 150rs")
else:
    print("Invalid Age! Please Enter Valid Age")
