'''Find the shortest word in a sentence. '''

text = "Python Is Easy language"
words = text.split()
shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i
print("Longest word is:",shortest)