'''count vowels of  string'''
name = input("Enter The Name : ")
count = 0

for i in name:
    if i in "aeiouAEIOU":
        count += 1
print("Total vowels:", count)
