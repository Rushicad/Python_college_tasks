'''
To check whether a year is a leap year and century year
'''

YEAR = int(input("Enter A Year: "))

if YEAR % 400 == 0:
    print("Year Is Leap Year and Century Year")
elif YEAR % 100 == 0:
    print("Year Is Not Leap Year but Century Year")
elif YEAR % 4 == 0:
    print("Year Is Leap Year but Not Century Year")
else:
    print("Year Is Not Leap Year and Not Century Year")
