rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

# THE CHOOSE OF THE USER
choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

# SHOWING THE OPTION THAT THE USER CHOSE
if choose == '0':
  print(rock)
elif choose == '1':
  print(paper)
else:
  print(scissors)

# SHOWING THE RANDOM VARIABLE
computer_random = [rock, paper, scissors]
random_option = random.choice(computer_random)
print(random_option)

# CHECKING WHO WIN
if choose == "0" and random_option == scissors:
  print("You Win!")
elif choose == "1" and random_option == rock:
  print("You Win!")
elif choose == "2" and random_option == paper:
  print("You Win!")
elif choose == "0" and random_option == rock:
  print("It's a draw, play it again.")
elif choose == "1" and random_option == paper:
  print("It's a draw, play it again.")
elif choose == "2" and random_option == scissors:
  print("It's a draw, play it again.")
else:
  print("You Lost!")



