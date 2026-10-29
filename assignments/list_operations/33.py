'''Create a list and find the second largest number'''

lst = [20, 60, 40, 10]

max_num = max(lst)
sec_max = 0

for i in lst:
    if i < max_num and i > sec_max:
        sec_max = i
print("Second Largest Number:", sec_max)