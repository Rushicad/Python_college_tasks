"""Create a movie ticket pricing program for a cinema. Ticket price depends on AGE,
show type, and whether the booking is on a weekend"""

CUSTOMER_NAME = input("Enter Your Name : ")
AGE = int(input("Enter Your Age : "))
SHOW_TYPE = input("Enter Show Type (Morning or Evening) : ").lower()
DAY_TYPE = input("Enter Day Type (Weekend or Weekday) : ").lower()
BASE_TICKET = 200
MORNING_SHOW = "morning"
EVENING_SHOW = "evening"
DAY1 = "weekend"
DAY2 = "weekday"

if DAY_TYPE == DAY1:
    SURCHARGE = 50
    print("Ticket Price Is Rs.", BASE_TICKET)
    if AGE >= 60:
        DIS = BASE_TICKET * (30 / 100)
        DIS_AMOUNT = BASE_TICKET - DIS
        FINAL_AMOUNT = SURCHARGE + DIS_AMOUNT
        print("You Got Discount Of Rs.", DIS)
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT - ADDITIONAL_DISCOUNT)
        elif SHOW_TYPE == EVENING_SHOW:
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT)
        else:
            print("Invalid Show")
    elif AGE >= 12 and AGE < 60:
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print(
                "Your Final Ticket Price Is Rs.",
                BASE_TICKET - ADDITIONAL_DISCOUNT + SURCHARGE,
            )
        elif SHOW_TYPE == EVENING_SHOW:
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print("Your Final Ticket Price Is Rs.", BASE_TICKET + SURCHARGE)
        else:
            print("Invalid Show")
    elif AGE > 5 and AGE < 12:
        DIS = BASE_TICKET * (50 / 100)
        DIS_AMOUNT = BASE_TICKET - DIS
        FINAL_AMOUNT = SURCHARGE + DIS_AMOUNT
        print("You Got Discount Of Rs.", DIS)
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT - ADDITIONAL_DISCOUNT)
        elif SHOW_TYPE == EVENING_SHOW:
            print("Weekend Surcharge Is Rs.", SURCHARGE)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT)
        else:
            print("Invalid Show")
elif DAY_TYPE == DAY2:
    print("Ticket Price Is Rs.", BASE_TICKET)
    if AGE >= 60:
        DIS = BASE_TICKET * (30 / 100)
        DIS_AMOUNT = BASE_TICKET - DIS
        FINAL_AMOUNT = DIS_AMOUNT
        print("You Got Discount Of Rs.", DIS)
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT - ADDITIONAL_DISCOUNT)
        elif SHOW_TYPE == EVENING_SHOW:
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT)
        else:
            print("Invalid Show")
    elif AGE >= 12 and AGE < 60:
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Your Final Ticket Price Is Rs.", BASE_TICKET - ADDITIONAL_DISCOUNT)
        elif SHOW_TYPE == EVENING_SHOW:
            print("Your Final Ticket Price Is Rs.", BASE_TICKET)
        else:
            print("Invalid Show")
    elif AGE > 5 and AGE < 12:
        DIS = BASE_TICKET * (50 / 100)
        DIS_AMOUNT = BASE_TICKET - DIS
        FINAL_AMOUNT = DIS_AMOUNT
        print("You Got Discount Of Rs.", DIS)
        if SHOW_TYPE == MORNING_SHOW:
            ADDITIONAL_DISCOUNT = 30
            print("You Got Additional Discount of Rs.", ADDITIONAL_DISCOUNT)
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT - ADDITIONAL_DISCOUNT)
        elif SHOW_TYPE == EVENING_SHOW:
            print("Your Final Ticket Price Is Rs.", FINAL_AMOUNT)
        else:
            print("Invalid Show")
    else:
        print("Enter Valid Age")
else:
    print("Enter Valid Day!")
