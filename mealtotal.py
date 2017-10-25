


#enter your total
meal_total = float(input("What is your total: "))
sales_tax = .07
tip = .18
total = (meal_total * sales_tax) + meal_total

real_total = (total * tip) + total

print ('Your total is', real_total)

