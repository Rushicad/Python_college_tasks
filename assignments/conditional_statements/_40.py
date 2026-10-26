'''
To check whether a password is valid using nested if.
'''

PASSWORD = '0809'
CORRECT = input("Enter The Password: ")

if CORRECT == PASSWORD:
    if PASSWORD == CORRECT:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Wrong Password")
