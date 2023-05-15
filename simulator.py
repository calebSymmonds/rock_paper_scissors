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

choice = input('Welcome to the rock, paper, scissors simulator.\nPlease select "Rock", "Paper", or "Scissors".\n').lower()

import random
import sys
computer_choice = random.randint(0, 2)

if choice == "rock":
  human_choice = 0
elif choice == "paper":
  human_choice = 1
elif choice == "scissors":
  human_choice = 2
else:
  print("Invalid input. Check your spelling and do not use quotation marks.")
  sys.exit()

print("You chose:")

if human_choice == 0:
  print(rock)
if human_choice == 1:
  print(paper)
if human_choice == 2:
  print(scissors)

print("The computer chose")

if computer_choice == 0:
  print(rock)
if computer_choice == 1:
  print(paper)
if computer_choice == 2:
  print(scissors)

if human_choice == computer_choice:
  print("It's a draw!")
if human_choice == 0 and computer_choice == 1:
  print("The computer wins. Sorry, pal.")
if human_choice == 1 and computer_choice == 2:
  print("The computer wins. Sorry, pal.")
if human_choice == 2 and computer_choice == 0:
  print("The computer wins. Sorry, pal.")
if computer_choice == 0 and human_choice == 1:
  print("You win!")
if computer_choice == 1 and human_choice == 2:
  print("You win!")
if computer_choice == 2 and human_choice == 0:
  print("You win!")
