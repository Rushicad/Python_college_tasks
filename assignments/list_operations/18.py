'''Take user input to create a list and display it.'''

lst =[]
size_lst = int(input("Enter Size Of List : "))
for i in range(size_lst):
    ele = input(f"Enter the {i} Element : ")
    lst.append(ele)
print(lst)