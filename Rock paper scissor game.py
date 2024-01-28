import random 

# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images=[rock,paper,scissors]

user_choice=int(input("What do you Chosse? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"you chose: {user_choice}")
if user_choice>=3 or user_choice<0:
    print("you type invalid no, You loose!")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print(f"computer chose: {computer_choice}")
    print(game_images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You Wins.")
    elif computer_choice==0 and user_choice==2:
        print("You Lose!")
    elif computer_choice>user_choice:
        print("You Lose!")
    elif user_choice>computer_choice:
        print("You Win.")
    elif user_choice==computer_choice:
        print("Match is Draw")





