'''Develop an insurance premium calculator. The premium category depends on age, 
occupation risk, and smoking status. '''


customer_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
risk = input("Enter Occupation Risk (Low/Medium/High): ").lower()
smoker = input("Are You a Smoker (Yes/No): ").lower()

base_premium = 10000
additional_charges = 0

print("\nCustomer Name:", customer_name)

if age < 18:
    print("You Are Not Eligible For Insurance")

else:
    if age > 50:
        additional_charges = additional_charges + 5000
    if risk == "high":
        additional_charges = additional_charges + 7000
    elif risk == "medium":
        additional_charges = additional_charges + 3000
    elif risk == "low":
        additional_charges = additional_charges + 0
    else:
        print("Invalid Occupation Risk")

    if risk == "low" or risk == "medium" or risk == "high":
        if smoker == "yes":
            additional_charges = additional_charges + 5000
        elif smoker == "no":
            additional_charges = additional_charges + 0
        else:
            print("Invalid Smoking Status")
        if smoker == "yes" or smoker == "no":
            final_premium = base_premium + additional_charges

            print("You Are Eligible For Insurance")
            print("Base Premium: Rs.", base_premium)
            print("Additional Charges: Rs.", additional_charges)
            print("Final Premium: Rs.", final_premium)

            if additional_charges >= 10000:
                print("Risk Message: High Risk Policy")
            else:
                print("Risk Message: Normal Risk Policy")
