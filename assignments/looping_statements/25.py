'''count consonants of  string'''
name = input("Enter The Name : ")
count = 0

for i in name:
    if i not in "aeiouAEIOU":
        count += 1
print("Total Consonants:", count)
