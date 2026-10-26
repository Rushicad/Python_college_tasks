'''Count number of digits in a number'''

nums = 4444
count = 0

while nums > 0:
    nums = nums // 10
    count += 1

print("Number of digits:", count)

 