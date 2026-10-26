'''
check whether a given year is a leap year or not.

'''
YEAR = int(input("Enter a Year : "))
if YEAR < 1000 or YEAR > 9999:
    print("Please enter a valid year")
elif YEAR % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
