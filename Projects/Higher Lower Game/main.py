from art import logo,vs
import random
from game_data import data
import os

def select_data():
    return random.choice(data)

def print_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f" {name}, {description}, {country}."
def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(logo)
    score = 0
    game_continue = True
    account_a = select_data()
    account_b = select_data()

    while game_continue:
        account_a = account_b
        account_b = select_data()

        while account_a == account_b:
            account_b = select_data()

        print(f"Compare A: {print_data(account_a)}")
        print(vs)
        print(f"Against B: {print_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess,a_follower_count,b_follower_count)

        os.system('cls')
        print(logo)
        if is_correct:
            score +=1
            print(f"You'r right. Your current score is {score}")
        else:
            game_continue = False
            print(f"Sorry That's wrong. Your score is {score}")

game()


