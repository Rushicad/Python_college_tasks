'''Create a list and demonstrate all list methods. '''


lst = [10, 20, 30, 20]

lst.append(40)
print("Append:", lst)

lst.extend([50, 60])
print("Extend:", lst)

lst.insert(1, 15)
print("Insert:", lst)

lst.remove(20)
print("Remove:", lst)

lst.pop()
print("Pop:", lst)

print("Index:", lst.index(30))

print("Count:", lst.count(20))

lst.sort()
print("Sort:", lst)

lst.reverse()
print("Reverse:", lst)

new_lst = lst.copy()
print("Copy:", new_lst)

lst.clear()
print("Clear:", lst)