'''Reverse a number using while loop'''

number = 1234
rev = 0
while number != 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10
print("The reverse number = ",rev)