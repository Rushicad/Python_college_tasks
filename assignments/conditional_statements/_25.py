'''
to check whether a triangle is equilateral, isosceles, or scalene

'''
SIDE_A = int(input("Enter Side A : "))
SIDE_B = int(input("Enter Side B : "))
SIDE_C = int(input("Enter Side C : "))
if SIDE_A == SIDE_B and SIDE_B == SIDE_C and SIDE_A == SIDE_C:
    print("The Triangle Is Equilateral Triangle")
elif SIDE_A == SIDE_B or SIDE_B == SIDE_C or SIDE_A == SIDE_C:
    print("The Triangle Is Isosceles Triangle")
else:
    print("The Triangle Is Scalene Triangle")
