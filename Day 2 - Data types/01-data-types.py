# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
if len(two_digit_number) == 2 and two_digit_number.isdigit():
    sum = int(two_digit_number[0]) + int(two_digit_number[1])
    #print(two_digit_number[0] + " + " + two_digit_number[1] + " = " + str(sum))
    print(sum)
else:
    print("Invalid input. Please enter a two-digit number with only digits.")