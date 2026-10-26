'''check whether a number is palindrome'''
num = int(input("Enter the Number : "))
original_num = num
rev = 0
while original_num > 0:
    digit = original_num % 10
    rev = rev *10 + digit
    original_num = original_num // 10
if rev == num:
    print('palindrome')
else:
    print("not palindrome")