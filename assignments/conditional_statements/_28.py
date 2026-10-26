'''
To calculate discounts based on total shopping amount.
'''

AMOUNT = int(input("Enter The Total Amount: "))

if AMOUNT >= 5000:
    DISCOUNT = AMOUNT * 20 / 100
    print("You Got 20% Discount")
elif AMOUNT >= 3000:
    DISCOUNT = AMOUNT * 10 / 100
    print("You Got 10% Discount")
elif AMOUNT >= 1000:
    DISCOUNT = AMOUNT * 5 / 100
    print("You Got 5% Discount")
else:
    DISCOUNT = 0
    print("No Discount")

print("Discount Amount:", DISCOUNT)
print("Final Amount:", AMOUNT - DISCOUNT)