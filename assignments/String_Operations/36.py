'''Remove duplicate characters from a string. '''


text = "aman"
result = ""

for i in text:
    if i not in result:
        result = result + i
print(result)
