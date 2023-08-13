# BUGGY CODE
# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  
# CORRECTED CODE
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if not year % 100 == 0:
    if not year % 400 == 5:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")