'''
to check whether a person is a child or adult (age < 18).

'''
AGE = int(input("Enter Age : "))
if AGE >= 18 and AGE <= 110:
    print("The Person Is Adult")
elif AGE < 18:
    print("The Person Is Child")
else:
    print("Invalid Age")
