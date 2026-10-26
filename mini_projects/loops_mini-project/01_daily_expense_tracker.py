''' Record expenses for a chosen number of days and summarize spending.'''

days = int(input("Enter Number Of Days : "))
total = 0
highest = 0

for i in range(1,days+1):
    expense = int(input("Enter Your Expense :"))
    total = total + expense
    if expense > highest:
        highest = expense
print("Total Expense Is :",total)
if total >= 5000:
     print("Budget Alert")
else:
     print("Budget In Control")
avg = total / days
print("avg of Daily Expense is",avg)
print("The Highest Expense Of The Day Is",highest)
 