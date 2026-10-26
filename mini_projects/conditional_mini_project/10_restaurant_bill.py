"""Create a restaurant billing program for a customer. The service charge and DISCOUNT
depend on the bill amount and membership status"""

CUSTOMER_NAME = input("Enter Your Name: ")
FOOD_BILL = float(input("Enter Your Food Bill Amount: "))
MEMBER_STATUS = input("Enter Your Membership Status (Yes/No): ").lower()

DISCOUNT = 0

if FOOD_BILL > 0:
    if FOOD_BILL < 1000:
        DISCOUNT = 0
    elif FOOD_BILL < 3000:
        DISCOUNT = 5
    elif FOOD_BILL < 5000:
        DISCOUNT = 10
    else:
        DISCOUNT = 15

    if MEMBER_STATUS == "yes":
        DISCOUNT = DISCOUNT + 5

    elif MEMBER_STATUS == "no":
        DISCOUNT = DISCOUNT

    else:
        print("Invalid Membership Status")

    if MEMBER_STATUS == "yes" or MEMBER_STATUS == "no":
        DISCOUNT_AMOUNT = FOOD_BILL * DISCOUNT / 100
        DISCOUNTED_BILL = FOOD_BILL - DISCOUNT_AMOUNT

        SERVICE_CHARGE = DISCOUNTED_BILL * 5 / 100
        FINAL_BILL = DISCOUNTED_BILL + SERVICE_CHARGE

        print("\nCustomer Name:", CUSTOMER_NAME)
        print("Original Bill: Rs.", FOOD_BILL)
        print("Discount: Rs.", DISCOUNT_AMOUNT)
        print("Service Charge: Rs.", SERVICE_CHARGE)
        print("Final Payable Amount: Rs.", FINAL_BILL)

        if FINAL_BILL >= 5000:
            print("Thank you for being a valued customer")
else:
    print("Invalid Bill Amount")
