"""Build a mobile data billing program for a telecom customer. The monthly bill
depends on the selected PLAN and additional data usage."""
CUSTOMER_NAME = input("Enter Your Name : ")
PLAN = input("Enter PLAN Type(Basic, Standard, Premium): ").lower()
EXTRA = float(input("Enter The Extra Data Used In GB : "))
B_PLAN = "basic"
S_PLAN = "standard"
P_PLAN = "premium"
print("Hey",CUSTOMER_NAME)

if PLAN == B_PLAN:
    PLAN = 299
    print("You Select The Basic Plan Rs.299 It Includes 10 GB")
    print("Base Plan Charge Is Rs.", PLAN)
    SURCHARGE = 100
    if EXTRA > 0:
        EXTRA_DATA = EXTRA * 20
        print("Extra Data Charge", EXTRA_DATA)
        if EXTRA >= 10:
            print("Surcharges Over 10 GB Is Rs.100")
            EXTRA_DATA = (EXTRA * 20) + SURCHARGE
            print("Your Final Bill Is Rs.", EXTRA_DATA + PLAN)
    else:
        print("Enter Valid Used Data")
elif PLAN == S_PLAN:
    PLAN = 499
    print("You Select The Standard Plan Rs.499 It Includes 25 GB")
    print("Base Plan Charge Is Rs.", PLAN)
    SURCHARGE = 100
    if EXTRA > 0:
        EXTRA_DATA = EXTRA * 20
        print("Extra Data Charge", EXTRA_DATA)
        if EXTRA >= 10:
            print("Surcharges Over 10 GB Is Rs.100")
            EXTRA_DATA = (EXTRA * 20) + SURCHARGE
            print("Your Final Bill Is Rs.", EXTRA_DATA + PLAN)
    else:
        print("Enter Valid Used Data")
elif PLAN == P_PLAN:
    PLAN = 799
    print("You Select The Premium Plan Rs.799 It Includes 50 GB")
    print("Base Plan Charge Is Rs.", PLAN)
    SURCHARGE = 100
    if EXTRA > 0:
        EXTRA_DATA = EXTRA * 20
        print("Extra Data Charge", EXTRA_DATA)
        if EXTRA >= 10:
            print("Surcharges Over 10 GB Is Rs.100")
            EXTRA_DATA = (EXTRA * 20) + SURCHARGE
            print("Your Final Bill Is Rs.", EXTRA_DATA + PLAN)
else:
    print("Enter Valid Info")
