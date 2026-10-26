"""
Create a checkout program for an online shopping website. The discount depends on
the purchase amount, and premium customers receive an additional benefit.
"""

C_NAME = input("Enter Your Name : ")
P_AMOUNT = int(input("Enter Your Purchase Amount : "))
CUSTOMER_TYPE = input("Enter Your Account Type Regular or Premium : ")
PRE = "premium" or "Premium" or "PREMIUM"
REG = "REGULAR", "Regular", "regular"
DELIVERY_CHARGES = 100


if P_AMOUNT >= 5000:
    DIS = P_AMOUNT * (20 / 100)
    ADD = P_AMOUNT - DIS
    ADD_DIS = P_AMOUNT * (5 / 100)
    ADDITIONAL_DISCOUNT = P_AMOUNT - ADD_DIS
    FINAL_DIS = DIS + ADD_DIS

    if CUSTOMER_TYPE in PRE:
        print("Your Discount Amount is Rs.", FINAL_DIS)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )

    elif CUSTOMER_TYPE in REG:
        print("Your Discount Amount Is Rs.", P_AMOUNT - ADD)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )
    else:
        print("Please Enter Valid Customer Type")

elif P_AMOUNT >= 3000 and P_AMOUNT < 5000:
    DIS = P_AMOUNT * (10 / 100)
    ADD = P_AMOUNT - DIS
    ADD_DIS = P_AMOUNT * (5 / 100)
    ADDITIONAL_DISCOUNT = P_AMOUNT - ADD_DIS
    FINAL_DIS = DIS + ADD_DIS
    FINAL_AMOUNT = P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES

    if CUSTOMER_TYPE in PRE:
        print("Your Additional Discount Amount is Rs.", FINAL_DIS)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )
    elif CUSTOMER_TYPE in REG:
        print("Your Discount Amount Is Rs.", P_AMOUNT - ADD)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )
    else:
        print("Please Enter Valid Customer Type")

elif P_AMOUNT >= 1000 and P_AMOUNT < 3000:
    DIS = P_AMOUNT * (5 / 100)
    ADD = P_AMOUNT - DIS
    ADD_DIS = P_AMOUNT * (5 / 100)
    ADDITIONAL_DISCOUNT = P_AMOUNT - ADD_DIS
    FINAL_DIS = DIS + ADD_DIS

    if CUSTOMER_TYPE in PRE:
        print("Your Additional Discount Amount is Rs.", FINAL_DIS)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )
    elif CUSTOMER_TYPE in REG:
        print("Your Discount Amount Is Rs.", P_AMOUNT - ADD)
        if P_AMOUNT - FINAL_DIS >= 2000:
            print("Free Delivery")
            print("Your Final Payable Amount is Rs.", P_AMOUNT - FINAL_DIS)
        else:
            print("The delivery charges are included")
            print(
                "Your Final Payable Amount is Rs.",
                P_AMOUNT - FINAL_DIS + DELIVERY_CHARGES,
            )
    else:
        print("Please Enter Valid Customer Type")
elif P_AMOUNT < 1000 or P_AMOUNT > 0:
    print("Delivery Charges Rs.", DELIVERY_CHARGES)
    print("Your Final Payable amount is Rs.", P_AMOUNT + DELIVERY_CHARGES)
else:
    if P_AMOUNT <= 0:
        print("Enter Correct Amount")
