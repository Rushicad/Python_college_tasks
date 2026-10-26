'''
To check salary bonus based on years of service.
'''

SALARY = int(input("Enter Your Salary: "))
YEARS = int(input("Enter Years Of Service: "))

if YEARS >= 10:
    BONUS = SALARY * 20 / 100
    print("You Got 20% Bonus")
elif YEARS >= 5:
    BONUS = SALARY * 10 / 100
    print("You Got 10% Bonus")
elif YEARS >= 2:
    BONUS = SALARY * 5 / 100
    print("You Got 5% Bonus")
else:
    BONUS = 0
    print("No Bonus")

print("Bonus Amount:", BONUS)
print("Total Salary With Bonus:", SALARY + BONUS)
