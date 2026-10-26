'''Print ASCII values of characters in a string. '''

text = input("Enter a string: ")

for i in text:
    print(i, "=", ord(i))
