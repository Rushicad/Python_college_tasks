'''Create an empty list and add 5 integers using append().'''

lst = []
for i in range(1,6):
    elements = input(f"Enter The {i} Element : ")
    lst.append(elements)
print(lst)