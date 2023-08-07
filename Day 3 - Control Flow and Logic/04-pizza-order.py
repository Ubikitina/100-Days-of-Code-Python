# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if not size.upper() in ['S', 'M', 'L']:
    print("Invalid size.")
    exit()

if not add_pepperoni.upper() in ['Y', 'N']:
    print("Invalid entry for pepperoni.")
    exit()

if not extra_cheese.upper() in ['Y', 'N']:
    print("Invalid entry for extra cheese.")
    exit()

# Define the prices of pizzas and toppings
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_small_price = 2
pepperoni_medium_large_price = 3
extra_cheese_price = 1

# Initialize the total bill with the base pizza price
total_bill = 0

# Add the price of the pizza based on the size
if size == 'S':
    total_bill += small_pizza_price
elif size == 'M':
    total_bill += medium_pizza_price
else:
    total_bill += large_pizza_price

# Check if the user wants pepperoni
if add_pepperoni == 'Y':
    # Add the appropriate pepperoni price based on the size
    if size == 'S':
        total_bill += pepperoni_small_price
    else:
        total_bill += pepperoni_medium_large_price

# Check if the user wants extra cheese
if extra_cheese == 'Y':
    # Add the extra cheese price
    total_bill += extra_cheese_price

print("Your final bill is: $" + str(total_bill) + ".")