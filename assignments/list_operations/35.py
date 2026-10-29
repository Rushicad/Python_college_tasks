'''Create a list and remove all even numbers.'''

lst = [10, 56, 98, 53, 11, 20]

for i in lst[:]:
    if i % 2 == 0:
        lst.remove(i)
print(lst)