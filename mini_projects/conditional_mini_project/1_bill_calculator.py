"""
Develop a small electricity billing program for a household. The electricity board
charges different rates according to the number of units consumed
"""

Customer_name = input("Enter Your Name : ")
UNITS = int(input("Enter The Numbers Of Consumed Unit : "))
FIXED = 150

if UNITS <= 100:
    SERVICES = UNITS * 3
    print("Your Energy Charges 3rs/Unit = ", SERVICES)
elif UNITS >= 101 and UNITS <= 200:
    SERVICES = UNITS * 5
    print("Your Energy Charges 5rs/Unit = ", SERVICES)
elif UNITS > 200:
    SERVICES = UNITS * 7
    print("Your Energy Charges 7rs/Unit = ", SERVICES)
else:
    print("Wrong Number")
FINAL = SERVICES + FIXED
print("Customer name : ",Customer_name)
print("Consumed Units : ",UNITS)
print("Your Fixed Service Charge is ",FIXED)
print("Your Final Bill Is : ",FINAL)
if FINAL >= 5000:
    print("High Usage Bill")
else:
    print("Usage in Limit")
