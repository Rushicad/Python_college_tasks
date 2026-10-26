"""Create a simple hotel booking calculator. The room PRICE depends on room type and
the number of NIGHTS. Customers may also receive a discount based on their stay."""

GUEST_NAME = input("Enter Your Name : ")
print("Enter Which Type of Room Do You Want?")
print(
    """Standard Room Rs.2000/Night \nDeluxe Room Rs.3500/Night \nSuite Room Rs.6000/Night"""
)
ROOM_TYPE = input("Standard, Deluxe, Suite : ").lower()
NIGHTS = int(input("Enter the Number Of Nights That You Have to Spend : "))
STD = "standard"
DELUXE = "deluxe"
SIT = "suite"
print("Hey", GUEST_NAME)

if ROOM_TYPE == STD:
    PRICE = 2000
    if NIGHTS >= 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (20 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)

    elif NIGHTS >= 5 and NIGHTS < 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (10 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)
    elif NIGHTS <= 5 and NIGHTS > 0:
        print("No Discount")
        print("Final Price:", PRICE)
    else:
        print("Enter Valid Nights To tay")
elif ROOM_TYPE == DELUXE:
    PRICE = 3500
    if NIGHTS >= 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (20 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)

    elif NIGHTS >= 5 and NIGHTS < 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (10 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)
    elif NIGHTS <= 5 and NIGHTS > 0:
        print("No Discount")
        print("Final Price:", PRICE)

    else:
        print("Enter Valid Nights To tay")
elif ROOM_TYPE == SIT:
    PRICE = 6000
    if NIGHTS >= 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (20 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)

    elif NIGHTS >= 5 and NIGHTS < 10:
        NIGHT = NIGHTS * PRICE
        DIS = NIGHT * (10 / 100)
        FINAL_PRICE = NIGHT - DIS
        print("You Select Standard Room")
        print("No.of Nights", NIGHTS)
        print("Original Price:", NIGHT)
        print("Discount Price:", DIS)
        print("Final Price:", FINAL_PRICE)
    elif NIGHTS <= 5 and NIGHTS > 0:
        print("No Discount")
        print("Final Price:", PRICE)
    else:
        print("Enter Valid Nights To Stay")
else:
    print("Invalid Room Type", ROOM_TYPE)
