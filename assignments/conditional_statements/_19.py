'''
to print the day name based on day number (1-7).

'''

NUM = int(input("Enter The Number : "))
match NUM:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday") 
    case 5:
        print("Friday") 
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number")

