'''
to check traffic signal actions using match case.

'''
SIGNAL = input("Enter Traffic Signal Color: ")

match SIGNAL:
    case "red" | "Red" |"RED":
        print("STOP")
    case "yellow" | "Yellow"| "YELLOW":
        print("WAIT")
    case "green" | "Green" |"GREEN":
        print("GO")
    case _:
        print("Invalid Traffic Signal")
