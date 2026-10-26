
'''Simulate ATM Access With Limited PIN Attempts'''

pin = 657845
attempt = 0

while attempt < 3:
    i_pin = int(input("Enter the PIN: "))
    attempt = attempt + 1

    if pin == i_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN!")

        if attempt < 3:
            print("Remaining Attempts:", 3 - attempt)
        else:
            print("Card Temporarily Locked")
print("Attempts Used:", attempt)
