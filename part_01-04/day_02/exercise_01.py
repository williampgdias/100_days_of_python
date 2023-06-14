# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# WARNING. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# HINT
# 1. Try to find out the data type of two_digit_number
# 2. Think about what you learnt about subscripting
# 3. Think about type conversion

# Don't change the code below 👇🏻
two_digit_number = input('Type a two digit number: ')
# Don't change the code above 👆🏻

####################
# Write your code below this line 👇🏻
first_number = two_digit_number[0]
second_number = two_digit_number[1]
result = int(first_number) + int(second_number)

print(result)