'''
to check blood donation eligibility based on age and weight
'''
AGE = int(input("Enter Your Age : "))
WEIGHT = int(input("Enter Your Weight : "))
if AGE >= 18 and WEIGHT >= 45:
    print("Your Are Eligible For Blood Donation")
else:
    print("You Are Not Eligible For Donation")
