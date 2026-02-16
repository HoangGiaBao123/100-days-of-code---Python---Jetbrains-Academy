# Welcome to Rock, Paper, Scissors game!
import random

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

options = [rock, paper, scissors]

random_num = random.randint(0, len(options) - 1)
computer_option = options[random_num]
player_option = int(input("What do you choose? (Rock: 1, Paper: 2, Scissors: 3): "))

if options[player_option - 1] == computer_option:
    print(options[player_option - 1])
    print(computer_option)
    print("Draw")

elif player_option == 1 and random_num == 1:
    print(options[player_option - 1])
    print(computer_option)
    print("You lose!")

elif player_option == 1 and random_num == 2:
    print(options[player_option - 1])
    print(computer_option)
    print("You win!")

elif player_option == 2 and random_num == 0:
    print(options[player_option - 1])
    print(computer_option)
    print("You win!")

elif player_option == 2 and random_num == 2:
    print(options[player_option - 1])
    print(computer_option)
    print("You lose!")

elif player_option == 3 and random_num == 1:
    print(options[player_option - 1])
    print(computer_option)
    print("You win!")

elif player_option == 3 and random_num == 0:
    print(options[player_option - 1])
    print(computer_option)
    print("You lose!")

else:
    print("Something is wrong!")
