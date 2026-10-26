''' Find sum of odd digits in a number.'''

number = 123465
total = 0
while number != 0:
    digit = number % 10
    if number %2 != 0:
        total = total + digit
    number = number // 10
print("The Addition of the number = ",total)