'''Print numbers until user enters a negative number. '''
total = 0
while True:
    num = int(input("Enter The Number: "))
    if num < 0:
        break
    total = total + num
print("Addition is:", total)