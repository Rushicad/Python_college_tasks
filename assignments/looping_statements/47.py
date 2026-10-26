'''Find product of digits of a number. '''
number = int(input("Enter the number : "))
total = 1
while number != 0:
    digit = number % 10
    total = total * digit
    number = number // 10
print("The Addition of the number = ",total)