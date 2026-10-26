''' Count uppercase and lowercase letters separately.'''

'''Count uppercase and lowercase letters separately.'''

text = "Python Is Easy Language"
upper = 0
lower = 0

for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

    