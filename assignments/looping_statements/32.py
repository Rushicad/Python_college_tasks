'''calculate power of a number without using pow()'''

num = int(input("Enter the Number : "))
num2 = int(input("enter the power number : "))
power = 1
for i in range(num):
    power = num ** num2
print("Power of number is : ",power)