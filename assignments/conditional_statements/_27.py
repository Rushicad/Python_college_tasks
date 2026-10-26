'''
to check login status based on username and password

'''
USERNAME = 'ABC'
PASSWORD = '123'
U_NAME = input("Enter The Username : ")
P_WORD = int(input("Enter The Password : "))
if U_NAME == USERNAME and P_WORD == PASSWORD:
    print("Login Successful")
else:
    print("Incorrect Username or Password")
