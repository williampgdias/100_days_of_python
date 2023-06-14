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


# TEACHER CODE
game_images = [rock, paper, scissors]

# THE CHOOSE OF THE USER
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if choose >= 3 or choose < 0:
  print("You typed an invalid number. You lose.")
else:
  print(game_images[choose])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])


  if choose == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and choose == 2:
    print("You lose!")
  elif computer_choice > choose:
    print("You lose!")
  elif choose > computer_choice:
    print("You win!")
  elif computer_choice == choose:
    print("It's a draw. Try again.")


#################### MY CODE! WORKING, BUT ITS BIGGER!!! ####################
# choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# SHOWING THE OPTION THAT THE USER CHOSE
# if choose >= "3" or choose < "0":
#   print("You typed an invalid number, you lose!")
# elif choose == "0":
#   print(rock)
# elif choose == "1":
#   print(paper)
# elif choose == "2":
#   print(scissors)

# SHOWING THE RANDOM VARIABLE
# computer_random = [rock, paper, scissors]
# random_option = random.choice(computer_random)
# print(random_option)
#
# # CHECKING WHO WIN
# if choose == "0" and random_option == scissors:
#   print("Rock breaks scissors. You Win! 👏🏻")
# elif choose == "1" and random_option == rock:
#   print("Paper wraps rock. You Win! 🕺🏻")
# elif choose == "2" and random_option == paper:
#   print("Scissors cuts paper. You Win! 💃🏻")
# elif choose == "0" and random_option == rock:
#   print("It's a draw, play it again.")
# elif choose == "1" and random_option == paper:
#   print("It's a draw, play it again.")
# elif choose == "2" and random_option == scissors:
#   print("It's a draw, play it again.")
# else:
#   print("I am sorry. You Lose! 😥")



