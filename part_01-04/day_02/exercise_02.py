# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Don't change the code below 👇🏻
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')
# Don't change the code above 👆🏻

# Write your code below this line 👇🏻
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# print(int(bmi))

# if bmi < 18.5:
#   print(f'Your BMI is: {bmi:.2f}\nYou are Underweight')
# elif 18.5 <= bmi <= 24.9:
#   print(f'Your BMI is: {bmi:.2f}\nYou are in your normal weight')
# elif 25 <= bmi <= 29.9:
#   print(f'Your BMI is: {bmi:.2f}\nYou are Overweight')
# else:
#   print(f'Your BMI is: {bmi:.2f}\nYou are Obese')
