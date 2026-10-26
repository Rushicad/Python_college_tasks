'''Find the longest word in a sentence'''


text = "Python is Easy language"
words = text.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i
print("Longest word is:", longest)


    