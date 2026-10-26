"""
Develop a salary BONUS calculator for a company. The BONUS depends on years of
experience and performance rating.
"""

EM_NAME = input("Enter The Name : ")
M_SALARY = int(input("Enter Your Monthly Salary : "))
Y_EX = int(input("Enter Your Years Of Experience : "))
RATE = float(input("Give Rating From 1 to 5 : "))

if Y_EX >= 10:
    if RATE >= 4 and RATE <= 5:
        BONUS = M_SALARY * (20 / 100)
        F_BONUS = M_SALARY + BONUS
        print("You Got 20% BONUS")
        print("Your Bonus Amount is : ", BONUS)
        print("Final Salary is : ", F_BONUS)
        print("Excellent performer")
    elif RATE > 5:
        print("Give Rating Between 1 to 5")
    else:
        print("No Bonus")
        print("Final Salary is : ", M_SALARY)


elif Y_EX >= 5 and Y_EX <= 9:

    if RATE > 3 and RATE < 5:

        BONUS = M_SALARY * (15 / 100)
        F_BONUS = M_SALARY + BONUS
        print("You Got 15% BONUS")
        print("Your Bonus Amount is : ", BONUS)
        print("Final Salary is : ", F_BONUS)

    else:
        print("No Bonus")
        print("Final Salary is : ", M_SALARY)

elif Y_EX >= 2 and Y_EX <= 4:

    if RATE >= 3 and RATE <= 4:
        BONUS = M_SALARY * (10 / 100)
        F_BONUS = M_SALARY + BONUS
        print("You Got 10% BONUS")
        print("Your Bonus Amount is : ", BONUS)
        print("Final Salary is : ", F_BONUS)
    else:
        print("No Bonus")
        print("Final Salary is : ", M_SALARY)

else:
    print("Less Years Of Experience")
