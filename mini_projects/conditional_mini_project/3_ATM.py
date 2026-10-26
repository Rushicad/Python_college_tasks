"""Build a simple ATM transaction program that allows a customer to withdraw money
after checking account balance and withdrawal limits."""

A_NAME = input("Enter Account Holder Name : ")
C_BALANCE = float(input("Enter The Current Balance : "))
WITH_AMT = float(input("Enter The Withdrawal Amount : "))
if WITH_AMT > 0 and C_BALANCE >= WITH_AMT:
    if WITH_AMT <= 20000:
        REM = C_BALANCE - WITH_AMT
        if REM < 1000:
            print("Balance is Low Rs.",REM)
    else:
        print("Maximum withdrawal allowed in one transaction is ₹20,000")
        print("Please Select Your withdrawal Amount Between ₹20,000")
    print(f"Account Holder {A_NAME}")
    print("Withdrawn amount is Rs.",WITH_AMT)
    print("Transaction successful")
    print("Remaining Amount Rs.",REM)
else:
    print("Enter The Valid Amount")
