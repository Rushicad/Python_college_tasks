'''calculate sum of cubes of first n numbers'''
num = int(input("Enter the Number: "))
cb = 0

for i in range(1, num + 1):
    cb = cb + (i * i * i)

print("Sum of squares:", cb)
