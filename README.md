# Tax-Bracket-Challenge

Progressive tax bracket challenge questions for Roostify dev positions

Roostify Take home assignment

# Question - Bracketed Tax Engine:

Write a program that calculates income tax based on the following rules:

- The portion of the income that is less than $10k is untaxed
  Income up to 10K, no tax
- The portion of the income that is less than $20k is taxed at 10%
  Income up to $20K, (num/100) \* 10
- The portion of the income that is less than $50k is taxed at 20%
  Income up to $50K, (num/100) \* 20
- Any portion of the income that is above $50k is taxed at 30%
  Income > $50K, (num/100)\*30

1. Assume this application will be used by a 3rd party tax consultant who will have to run this for 100 clients.  
   Write a program that is scalable.
   The program should take the $ income and return the tax amount.
2. Imagine there are actually 50+ brackets that change every year, and we need to compute 1 Billion income tax projections every year.  
   Describe in a few bullet points how you’d build a solution that scales.
