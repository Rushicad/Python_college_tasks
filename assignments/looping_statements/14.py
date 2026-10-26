'''print fibonacci series up to n terms'''


num1 = int(input("Enter The Ending number : "))

a = 0
b = 1
for i in range(num1):
    print(a)
    next_num = a+b
    a=b
    b=next_num

    