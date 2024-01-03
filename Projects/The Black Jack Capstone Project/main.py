from art import logo
import random
print(logo)

user_cards = []
computer_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



#Hint 9: Call calculate_score().
# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
is_game_over = False
for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_result = calculate_score(user_cards)
computer_result = calculate_score(computer_cards)
print(user_result)
print(computer_result)
if user_result == 0 or computer_result == 0 or user_result > 21:
    is_game_over = True
    print("game ends")