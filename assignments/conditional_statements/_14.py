'''
to check whether a given character is uppercase or lowercase

'''
CHAR = input("Enter the Character : ")
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
if CHAR in UPPER:
    print("The Given Character is Uppercase")
elif CHAR in LOWER:
    print("The Given Character is Lowercase")
else:
    print("Invalid Identity")
