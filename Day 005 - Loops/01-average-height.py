# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() # e.g. input = 180 124 165 173 189 169 146
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# We cannot use len() and sum() functions
total_height = 0
count = 0
for n in range(0, len(student_heights)):
  total_height = total_height + student_heights[n]
  count = count +1

print(round(total_height/count))

