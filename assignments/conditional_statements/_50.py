'''
To build a simple ATM menu using match case.
'''

print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")
print("4. Exit")

CHOICE = int(input("Enter Your Choice (1-4): "))

match CHOICE:
    case 1:
        print("Your Balance Is: ₹5000")

    case 2:
        print("Please Collect Your Money")

    case 3:
        print("Money Deposited Successfully")

    case 4:
        print("Thank You For Using ATM")

    case _:
        print("Invalid Choice")
