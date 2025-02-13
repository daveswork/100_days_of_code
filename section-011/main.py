import random
import art


def deal_card() -> int:
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)

def calculate_score(cards:list) -> int:
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def print_current_user_score(user_cards, user_total, comp_cards, comp_total ):
    print(f"Your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {comp_cards[0]}")

def print_final_score(user_cards, user_total, comp_cards, comp_total):
    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_total}")

do_you_want_to_play = 'y'

while do_you_want_to_play == 'y':
    do_you_want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if do_you_want_to_play == 'n':
        break
    print(art.logo)
    your_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    your_total = calculate_score(your_cards)
    computer_total = calculate_score(computer_cards)
    print_current_user_score(your_cards, your_total, computer_cards, computer_total)
    if your_total > 21:
        print("You went over. You lose 😭")
        print_final_score(your_cards, your_total, computer_cards, computer_total)
        continue
    another_card = "y"
    while another_card == "y":
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            your_cards.append(deal_card())
            your_total = sum(your_cards)
            if your_total > 21:
                print("You went over. You lose 😭")
                print_final_score(your_cards, your_total, computer_cards, computer_total)
                break
            print_current_user_score(your_cards, your_total, computer_cards, computer_total)
        else:
            break
    while computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = sum(computer_cards)
    if computer_total == your_total:
        print("It's a draw.")
    elif computer_total <= 21 and computer_total > your_total:
        print_final_score(your_cards, your_total, computer_cards, computer_total)
        print("You lose 😤")
    else:
        print_final_score(your_cards, your_total, computer_cards, computer_total)
        print("You win 😃")

