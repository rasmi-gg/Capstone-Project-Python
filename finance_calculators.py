import math
investment_or_bond = str(input('''Choose either 'Investment' or 'Bond' from the menu below to proceed:
\n Investment: to calculate the amount of interest you'll earn in interest
\n Bond: to calculate the amount you'll have to pay on a home loan ''')).lower()

#introducing and defining appropriate input variables for investment conditionals 
if investment_or_bond  == "investment":
     p = float(input("How much are you depositing? ")) 
     interest_rate = float(input(" What is the interest rate " )) 
     r = interest_rate / 100 
     t = float(input("How many years are you investing it for? "))  
     type_of_interest = str(input("Choose your preferred interest: Simple or Compound ")).lower() 
     if type_of_interest == "simple":
            total_interest = p*(1 + r * t) 
            print(f"The total amount interest you will earn after {t} years is {total_interest}")
     elif type_of_interest == "compound": 
            total_interest= p*math.pow((1+r),t) 
            print(f"The total amount of interest you will earn after {t} years is {total_interest}")

# introducing Bond as another conditional 
elif investment_or_bond == "bond":
    p = float(input("What is the present value of the house ")) 
    interest_rate = float(input(" What is the annual interest rate" )) 
    i = (interest_rate/100)/12
    n = float(input("In how many months do you have to repay the bond ")) 
    monthly_amount = (i * p)/(1 - (1 + i)**(-n))
    print(f"The total amount you need to repay each month is {monthly_amount}")

#conditional for when the user enters an invalid input 
else:
    print("You did not enter a valid input. Please try again! ") 
    