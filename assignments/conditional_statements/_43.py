'''
to print month days using match case

'''
MONTH = int(input("Enter Month Number (1-12): "))

match MONTH:
    case 1:
        print("January - 31 Days")
    case 2:
        print("February - 28 or 29 Days")
    case 3:
        print("March - 31 Days")
    case 4:
        print("April - 30 Days")
    case 5:
        print("May - 31 Days")
    case 6:
        print("June - 30 Days")
    case 7:
        print("July - 31 Days")
    case 8:
        print("August - 31 Days")
    case 9:
        print("September - 30 Days")
    case 10:
        print("October - 31 Days")
    case 11:
        print("November - 30 Days")
    case 12:
        print("December - 31 Days")
    case _:
        print("Invalid Month Number")
