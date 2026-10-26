'''Check whether a string is a palindrome.'''


name = input("Enter the String: ")
rev = name[::-1]
if name == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
