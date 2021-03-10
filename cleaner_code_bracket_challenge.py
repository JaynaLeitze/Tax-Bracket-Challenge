# Write a program that calculates income tax based on the following rules:

# - The portion of the income that is less than $10k is untaxed
# - The portion of the income that is less than $20k is taxed at 10%
# - The portion of the income that is less than $50k is taxed at 20%
# - Any portion of the income that is above $50k is taxed at 30%

# 1. Assume this application will be used by a 3rd party tax consultant who will have to run this for 100 clients.  
#    Write a program that is scalable.
#    The program should take the $ income and return the tax amount.

#Define a fuction that takes income as a parameter and returns tax by using dictionary with values
# and a for loop that takes in the values from the dictionary to compute tax amount
def tax(income):
    #create dictionary of income bracket values
    income_cap = {50000:0.30, 20000:0.1,10000:0.0}
    #set initial tax variable to zero
    total_tax = 0
    #create for loop for values in dictionary
    for value in income_cap:
        #create conditional to return tax amount based on income
        if income >= value:
            tax_percent = income_cap.get(value)
            sum_to_tax_from = income - value
            total_tax += (sum_to_tax_from * tax_percent)
            income -= sum_to_tax_from
    return int(total_tax)


    