# Write a program that calculates income tax based on the following rules:

# - The portion of the income that is less than $10k is untaxed
# - The portion of the income that is less than $20k is taxed at 10%
# - The portion of the income that is less than $50k is taxed at 20%
# - Any portion of the income that is above $50k is taxed at 30%

# 1. Assume this application will be used by a 3rd party tax consultant who will have to run this for 100 clients.  
#    Write a program that is scalable.
#    The program should take the $ income and return the tax amount.

#Define variables of income brackets:
fifty = 50000
twenty = 20000
ten = 10000

#Define variables that compute tax 
tax_on_10k = 0
tax_on_20k = int((20000 - 10000)*0.1)
tax_on_50k = int((50000-30000)*0.2) + tax_on_20k

#Define a function that takes income amount as a parameter and returns tax amount on income given
def tax(income):
    #set initial tax to zero
    tax_amount = 0
    #conditionally render tax for income greater than fifty
    if income > fifty:
        tax_amount += int((income - fifty)*0.3 + tax_on_50k)
    #conditionally render tax for income greater than 20, less than 50
    elif income >twenty:
        tax_amount += int((income-twenty)*0.1 +tax_on_20k)
    #conditionally render tax for income greater than 20, less than 20
    elif income > ten:
        tax_amount += int((income - ten) + tax_on_10k)
    #return tax amount
    return(tax_amount)

#test output with print statements
print(tax(30000))
print(tax(75000))
print(tax(15000))
print(tax(10000))

#This file helped me to think through the problem itself. 
#Variables are clearly defined, but not very clean and concise
