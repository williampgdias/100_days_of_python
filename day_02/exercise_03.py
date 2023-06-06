# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old
# It will take your current age as the input and output a message with our time left in this format:
# You have X days, Y weeks, and Z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# WARNING your output should match the words in the example output precisely. You should round the results to the nearest whole number.

# HINT
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Don't change the code below
age = input("What is your current age? ")

# Write your code below this line
age_as_int = int(age)

target_age = 90
years_remaining = target_age - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(message)


