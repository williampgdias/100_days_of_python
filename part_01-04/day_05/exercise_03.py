# Write a program that calculates the sum of all the EVEN numbers from 1 to 100, including 1 and 100.

# e.g. 2 + 4 + 6 + 8 + 10 ... + 98 + 100

# Important, there should only be 1 print statement in the console output. It should just print the final total and not
# every step of the calculation.

# ONE WAY TO SOLVE THE CHALLENGE
total = 0
for number in range(2, 101, 2):
  total += number

print(total)

# ANOTHER WAY TO SOLVE THE CHALLENGE
total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)