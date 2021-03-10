fifty = 50000
twenty_k = 20000
ten_k = 10000

# tax_on_10k = 0
tax_on_20k = int((20000 - 10000)*0.1)
tax_on_50k = int((50000-20000)*0.2) + ((20000 - 10000)* 0.1)
#tax_over_50k = int((50000 - 30000)*0.2 + (20000 - 10000)*0.1) + (())

def tax(num):
    tax_amount = 0
    if num > fifty:
        tax_amount += int((num - fifty)*0.3 + tax_on_50k)  
    elif num > twenty_k:
        tax_amount += int((num - twenty_k)*0.20 + tax_on_20k)  
    elif num > ten_k:
        tax_amount += int((num - ten_k)* 0.1 ) 
    
    return(tax_amount)

print(tax(30000))
print(tax(75000))
print(tax(15000))
print(tax(10000))