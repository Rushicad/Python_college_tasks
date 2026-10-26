'''find largest digit in a number'''

number = 1234
total = 0
while number != 0:
    digit = number % 10
    total = total +1
    if digit > number:
        print("The Largest of the number = ",digit)
        