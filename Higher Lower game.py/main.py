from game_data import data
from art import logo,vs
import os
import random

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def formate_data(account):
    """Formating the data  into printable formate : name,description ,country """
    name=account["name"]
    description=account["description"]
    country=account["country"]

    return f"{name},a {description},from {country}"

def check_answer(guess,a_followers,b_followers):
    """Checking if guess is correct or not and returning result accordingly"""
    if a_followers>b_followers:
        return guess=="a"
    else:
        return  guess=="b"

def game():
    """The main function of the game"""
    print(logo)
    score=0
    game_should_continue=True
    account_a=get_random_account()
    account_b=get_random_account()

    while game_should_continue:
        account_a=account_b
        account_b=get_random_account()

        while account_a==account_b:
            account_b=get_random_account()

        print(f"Compare A: {formate_data(account_a)}.")
        print(vs)
        print(f"Compare B: {formate_data(account_b)}.")

        guess=input("Who has more followers? Type'A' or 'B':").lower()

        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        is_correct=check_answer(guess,a_follower_count,b_follower_count)
        os.system('cls')
        print(logo)
        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue=False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
again=input("Do you want to play it again 'Y' or 'N': ").capitalize()
if again=="Y":
    os.system("cls")
    game()
else:
    print("Thaks for playing this game")
    os.system("cls")

