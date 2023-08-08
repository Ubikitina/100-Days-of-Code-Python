# You are going to write a program that calculates the highest score from a List of scores.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split() # example input = 78 65 89 86 55 91 64 89
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# you are not allowed to use the max or min functions
max_score = 0
for n in range(0, len(student_scores)):
  if max_score < student_scores[n]:
    max_score = student_scores[n]
print("The highest score in the class is: {}".format(max_score))