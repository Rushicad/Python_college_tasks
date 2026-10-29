'''Create a list and check palindrome list.'''

lst = [10, 20, 30, 20, 10]
if lst == lst[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome List")