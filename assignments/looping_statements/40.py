'''print numbers which are perfect squares between 1 and 100'''
for i in range(1, 101):
    for j in range(1, 11):
        if j * j == i:
            print(i)