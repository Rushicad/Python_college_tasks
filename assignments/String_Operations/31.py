'''Remove punctuation marks from a string.'''

message = "Hello, Ritesh! How are you?"

for i in message:
    if i.isalnum() or i == " ":
        print(i, end="")
