'''Create a list of 10 numbers and remove duplicates.'''

lst = [10, 56, 78, 56, 98, 12, 10, 98, 12, 85]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)