
'''Find smallest digit in a number'''

num = 8784455641
small = 9
while num > 0:
    digit = num % 10
    if digit < small:
        small = digit
    num = num // 10
print("Smallest digit is:", small)
