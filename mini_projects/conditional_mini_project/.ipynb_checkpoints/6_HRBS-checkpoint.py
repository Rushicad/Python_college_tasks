"""Create a simple hotel booking calculator. The room price depends on room type and
the number of nights. Customers may also receive a discount based on their stay."""

guest_name = input("Enter Your Name : ")
print("Enter Which Type of Room You Want")
room_type = input("Standard, Deluxe, Suite : ")
nights = int(input("Enter the Number Of Nights That You Have to Spend : "))
std = 2000
delx = 3500
sit = 6000
print("Hey", guest_name)


if nights >= 5 and nights <= 9:
    if room_type == "Standard" or "standard" or "STANDARD":
        print("You Selected Standard Room")
        print("The Charges of Standard Room is Rs.2000/night")
        charges = std * nights
        print("You Got Special Discount Of 10%")
        dis = charges * (10 / 100)
        f_dis = charges - dis
    elif room_type == 'Deluxe' or 'DELUXE' or 'deluxe':
            print("You Selected Deluxe Room")
            print("The Charges of Deluxe Room is Rs.3500/night")
            charges = delx * nights
            print("You Got Special Discount Of 10%")
            dis = charges * (10 / 100)
            f_dis = charges - dis
    elif room_type == 'Suite' or 'suite' or 'SUITE':
            print("You Selected Deluxe Room")
            print("The Charges of Suite Room is Rs.6000/night")
            charges = delx * nights
            print("You Got Special Discount Of 10%")
            dis = charges * (10 / 100)
            f_dis = charges - dis
    else:
        print("Enter Valid Room type")


if nights >= 10:
    if room_type == "Standard" or "standard" or "STANDARD":
        print("You Selected Standard Room")
        print("The Charges of Standard Room is Rs.2000/night")
        charges = std * nights
        print("You Got Special Discount Of 20%")
        dis = charges * (20 / 100)
        f_dis = charges - dis
    elif room_type == 'Deluxe' or 'DELUXE' or 'deluxe':
            print("You Selected Deluxe Room")
            print("The Charges of Deluxe Room is Rs.3500/night")
            charges = delx * nights
            print("You Got Special Discount Of 20%")
            dis = charges * (20 / 100)
            f_dis = charges - dis
    elif room_type == 'Suite' or 'suite' or 'SUITE':
            print("You Selected Suite Room")
            print("The Charges of Deluxe Room is Rs.6000/night")
            charges = delx * nights
            print("You Got Special Discount Of 20%")
            dis = charges * (20 / 100)
            f_dis = charges - dis
    else:
        print("Enter Valid Room type")

        
    

    
        
        
    
    
    


print(f"Your Stay Is About to {nights} Nights ")
print("Your Room Charge is: ", charges)
print("Your Final Booking Amount is: ", f_dis)