'''
to print language choice using match case
'''
print("1. Marathi")
print("2. Hindi")
print("3. English")
print("4. Tamil")
LANG = int(input("Enter The Number(1-4) : "))
match LANG:
    case 1:
        print("Ohh! You Select Marathi")
    case 2:
        print("Ohh! You Select Hindi")
    case 3:
        print("Ohh! You Select English")
    case 4:
        print("Ohh! You Select Tamil") 
    case _:
        print("Invalid Number")
