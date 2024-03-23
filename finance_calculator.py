# Finance Calculator provides a way for user to build a calculation into either "investment", "bond", "simple" and "compound".

import math as math 

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# User chooses either 'investment' or 'bond'
# Variable is converted to lower-case in case they capitalise any part of the words

option = string(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))
choice = option.lower()

# If the user provides anything other than the specified terms they should receive an error message

if choice == "investment" or choice == "bond":
    print("Good choice! Let's continue.")

else:
    print("Error Message - invalid entry. Please refresh and try again.")

# Depending on the user choice of 'investment' or 'bond', they will be asked to input specific information relating to either choice
# If investment is chosen then they also need to decide if the interest is going to be 'simple' or 'compound'.

if choice == "investment":
    deposit = int(input("Please enter the amount you are attempting to deposit: "))
    inv_interest = int(input("Please enter the interest rate without the percentage symbol: "))
    years = int(input("Please enter the number of years you plan on investing: "))
    type = input("Please choose either 'simple' or 'compound' interest: ")
    r = inv_interest / 100

    if choice == 'investment' and type == 'simple':
        s_invest = round(deposit * (1 + r * years), 2)
        print(f"At the specified interest rate of {inv_interest}%, the amount that will be given back to you after {years} is £{s_invest}.")

    elif choice == 'investment' and type == 'compound':
        c_invest = round(deposit * math.pow((1 + r), years), 2)
        print(f"At the specified interest rate of {inv_interest}%, the amount that will be given back to you after {years} is £{c_invest}.")

elif choice == "bond":
    house_value = int(input("Please enter the value of the house: "))
    bond_interest = int(input("Please enter the interest rate without the percentage symbol: "))
    months_passed = int(input("Please enter the number of months you plan to take to repay the bond: "))
    i = (bond_interest / 100) / 12

    if choice == 'bond':
        repayment = round((i * house_value) / (1 - (1 + i) ** (- months_passed)), 2)
        print(f"Over the course of {months_passed}, this is how much money you will have to repay each month: £{repayment}.")
