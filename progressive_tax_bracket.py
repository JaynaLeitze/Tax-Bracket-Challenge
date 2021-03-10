# Write a program that calculates income tax based on the following rules:

# - The portion of the income that is less than $10k is untaxed
# - The portion of the income that is less than $20k is taxed at 10%
# - The portion of the income that is less than $50k is taxed at 20%
# - Any portion of the income that is above $50k is taxed at 30%

# 1. Assume this application will be used by a 3rd party tax consultant who will have to run this for 100 clients.  
#    Write a program that is scalable.
#    The program should take the $ income and return the tax amount.


#Define variables of income brackets:
tax_bracket_3 = 50000
tax_bracket_2 = 20000
tax_bracket_1 = 10000

#Define variables that compute tax 
tax_on_20k = (tax_bracket_2 - tax_bracket_1)*0.1
tax_on_50k = (tax_bracket_3-tax_bracket_2)*0.2 + tax_on_20k


#Define a function that takes income amount as a parameter and returns tax amount on income given
def tax(income):
    #set initial tax to zero
    tax_amount = 0
    #conditionally render tax for income greater than fifty
    if income > tax_bracket_3:
        tax_amount += int((income - tax_bracket_3)*0.3) + tax_on_50k 
    #conditionally render tax for income between tax bracket 2 and tax bracket 3
    elif income > tax_bracket_2:
        tax_amount += int((income - tax_bracket_2)*0.20) + tax_on_20k  
    #conditionally render tax for income between tax bracket 1 and tax bracket 2
    elif income > tax_bracket_1:
        tax_amount += int((income - tax_bracket_1)* 0.1)
    
    return(tax_amount)

#test output with print statements
print(tax(30000))
print(tax(75000))
print(tax(15000))
print(tax(10000))
 
#With income bracket and tax computation variables clearly defined, 
#tax bracket variables should be the only things that would need to be changed for this function
