#This script will calculate the user’s monthly savings based on inputted monthly income and expenses.
#It will then project these savings over a year, assuming a fixed interest rate, 
#to demonstrate compoundinterest’s effect on savings.

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
interest_rate = 0.5

#to calcualte monthly savings
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $",monthly_savings,".")

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", "$",projected_savings,".")

