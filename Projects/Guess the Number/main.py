from art import logo
import random
from replit import clear


def check_number(guess_the_num, number, attempts):
    if guess_the_num > number:
        print("Too high")
        attempts -= 1
        print("Guess again")
        return f"You have {attempts} attempts remaining to guess the number.", attempts
    elif guess_the_num < number:
        print("Too Low")
        attempts -= 1
        print("Guess again")
        return f"You have {attempts} attempts remaining to guess the number.", attempts
    elif guess_the_num == number:
        attempts = 0
        return f"You are correct. You guessed {guess_the_num}.", attempts


def num_guess():
    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    number = random.choice(range(1, 101))
    final_result = False
    attempts = 0
    if level == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif level == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("Kindly type 'easy' or 'hard' only.")
        final_result = True

    while not final_result or attempts > 0:
        guess_the_num = int(input("Make a guess: \n"))
        result_check, attempts = check_number(guess_the_num=guess_the_num, number=number, attempts=attempts)
        print(result_check)

        if attempts == 0:
            print("You are out of attempts")
            final_result = True


num_guess()
while input("Do you want to continue. Type 'Yes' or 'no' \n") == 'yes':
    clear()
    num_guess()
