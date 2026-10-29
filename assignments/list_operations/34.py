'''Create a list and find common elements between two lists.'''

lst1 = [10, 20, 60, 50]
lst2 = [50, 45, 65, 80]

for i in lst1:
    if i in lst2:
        print(i)