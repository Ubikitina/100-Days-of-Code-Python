# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if not year % 100 == 0:
        if not year % 400 == 5:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
     print("Not leap year.")   
else:
    print("Not leap year.")