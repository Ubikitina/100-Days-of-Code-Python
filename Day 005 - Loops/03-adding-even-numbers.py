# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100
#Write your code below this row 👇

total_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        total_sum = total_sum + i

print(total_sum)