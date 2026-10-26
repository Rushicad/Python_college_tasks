'''
to check user role (admin, user, guest) using match case
''' 
ROLE = input("Enter Your Role : ")
match ROLE:
    case'ADMIN'|'admin'|'Admin':
        print("Welcome Admin")
    case'User'|'USER'|'user':
        print("Welcome User")
    case'Guest'|'GUEST'|'guest':
        print("Welcome Guest")
    case _:
        print("Invalid Role")
