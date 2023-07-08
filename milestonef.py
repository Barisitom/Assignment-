#I added input for type of meal and percentage of Adult and Child Meal 
meal_type = input('\nWhat type of meal do yo have? ')
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
number_child = int(input("How many children are there? "))
number_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

child_sub_total = number_child * child_meal
adult_sub_total = number_adult * adult_meal

meal_sub_total = child_sub_total + adult_sub_total
print(f'\nMeal Subtotal: ${meal_sub_total:.2f}' )

percentage_of_child_meal = round(child_sub_total / meal_sub_total * 100)
print(f'Percentage of Child Meal: {percentage_of_child_meal}%' )

percentage_of_adult_meal = round(adult_sub_total / meal_sub_total * 100)
print(f'Percentage of Adult Meal: {percentage_of_adult_meal}%' )

sales_tax = float(meal_sub_total) * tax_rate/100
print(f'Sales Tax:  ${sales_tax:.2f}')

total_price = float(meal_sub_total) + float(sales_tax)
print(f'Total: ${total_price:.2f}' )

payment_amount = float(input('\nWhat is payment amount? '))

change = payment_amount - float(total_price)
print(f'Change: ${change:.2f}\n')