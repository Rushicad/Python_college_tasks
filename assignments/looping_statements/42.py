'''Calculate sum of squares of first n numbers'''

num = int(input("Enter the Number: "))
sq = 0

for i in range(1, num + 1):
    sq = sq + (i * i)
print("Sum of squares:", sq)
