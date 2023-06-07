# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

# Easiest way to solve the problem, but we can't use the sum() and the len() function to solve it.
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)


total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

print(round(total_height / number_of_students))