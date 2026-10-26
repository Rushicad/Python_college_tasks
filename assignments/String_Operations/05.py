''' Count the number of  Consonants in a string.
'''

name = "rushikesh"
vowels = "aeiouAEIOU"
count = 0

for i in name:
    if i not in vowels:
        count += 1
print("Total Consonants:", count)

    