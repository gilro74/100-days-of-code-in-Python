import random

print("Welcome to Rock, Paper and Scissor game!")
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

list_of_choices = ["rock","paper","scissors"]
user_choice = str(input('Please choose between "rock", "paper" or "scissors" :\n').strip().lower())
computer_choices = random.choice(list_of_choices)

if user_choice == "rock" and computer_choices == "paper":
    print(f"You chose rock{rock} \nand the computer chose paper{paper} \n So,You loose!")
elif user_choice == "rock" and computer_choices == "scissors":
    print(f"You chose rock{rock} \nand the computer chose scissors{scissors} \n So,You Win!")   
elif user_choice == "rock" and computer_choices == "rock":
    print(f"You chose rock{rock} \nand the computer chose rock{rock} \n So,it's a draw!")
elif user_choice == "paper" and computer_choices == "paper":
    print(f"You chose paper{paper} \nand the computer chose paper{paper} \n So,it's a draw!")
elif user_choice == "paper" and computer_choices =="rock":
    print(f"You chose paper{paper} \nand the computer chose rock{rock} \n So,You win!")
elif user_choice == "paper" and computer_choices == "scissors":
    print(f"You chose paper{paper} \nand the computer chose scissors{scissors} \n So,You loose!")
elif user_choice == "scissors" and computer_choices == "scissors":
    print(f"You chose scissors{scissors} \nand the computer chose scissors{scissors} \n So,it's a draw!")
elif user_choice == "scissors" and computer_choices == "paper":
    print(f"You chose scissors{scissors} \nand the computer chose paper{paper} \n So,it's a draw!")
elif user_choice == "scissors" and computer_choices =="rock":
    print(f"You chose scissors{scissors} \nand the computer chose rock{rock} \n So,You loose!")
else:
    print('Invalid input!. Please choose between "rock","paper" or "scissors"')

