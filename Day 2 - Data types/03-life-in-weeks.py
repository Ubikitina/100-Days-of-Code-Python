# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if age.isdigit():
    days = (90 - int(age))*365 # 365 days per year
    weeks = (90 - int(age))*52 # 52 weeks per year
    months = (90 - int(age))*12 # 12 months per year
    print("You have {} days, {} weeks, and {} months left.".format(days, weeks, months))
else:
    print("Incorrect entry. Please, enter a number.")



