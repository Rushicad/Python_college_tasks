'''Calculate factorial of a number using for loop'''
n = int(input("Enter The Number : "))
fact_n = 1
for i in range(1,n+1):
    fact_n = fact_n * i
print("factorial of Number is : ",fact_n)
    
    