''' Check whether a string is palindrome. '''


name = input("Enter a string: ")
rev = ""
i = len(name) - 1
while i >= 0:
    rev = rev + name[i]
    i -= 1
if name == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
