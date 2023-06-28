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

player_choice_digit = input('What do you choose? Type "0" for Rock, "1" for  Paper and "2" for Scissors.')
if int(player_choice_digit) >= 3:
    print("Invalid number!")
    exit()
player_choice = options[int(player_choice_digit)]
computer_choice = options[random.randint(0, 2)]

print(player_choice)
print("Computer chose:")
print(computer_choice)

if player_choice == computer_choice:
    print("Draw! Try again.")
elif player_choice == options[0] and computer_choice == options[1]:
    print("You lose!")
elif player_choice == options[0] and computer_choice == options[2]:
    print("You win!")
elif player_choice == options[1] and computer_choice == options[0]:
    print("You win!")
elif player_choice == options[1] and computer_choice == options[2]:
    print("You lose!")
elif player_choice == options[2] and computer_choice == options[0]:
    print("You lose!")
elif player_choice == options[2] and computer_choice == options[1]:
    print("You win!")







