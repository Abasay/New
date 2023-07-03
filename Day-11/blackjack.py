from art import logo
import random

print(logo)
player_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card(cards = cards):
    """Fuction to choose random card"""
    return random.choice(cards)

player_cards.append(pick_card())
computer_cards.append(pick_card())
should_play = input("Do you want to play the blackjack game? Type 'y' to play 'n' for no: ")
computer_first_card = computer_cards[0]

getCard='y'
computer_choice_list = ['y', 'n']


def winner_func(player_result, computer_result):
     """The function to print the winner"""
     if player_result > 21:
          print(f"       Your final hand: {player_cards}, final score: {player_result}")
          print(f"       Computer's final hand: {computer_cards}, final score: {computer_result}")
          print("You went over. You lose")
          return False
     elif computer_result > 21:
          print(f"       Your final hand: {player_cards}, final score: {player_result}")
          print(f"       Computer's final hand: {computer_cards}, final score: {computer_result}")
          print("Opponent went over. You win")
          return False
     elif player_result < computer_result and computer_result <= 21:
          print(f"       Your final hand: {player_cards}, final score: {player_result}")
          print(f"       Computer's final hand: {computer_cards}, final score: {computer_result}")
          print("You went over. You lose")
          return False
     elif player_result == computer_result:
          print(f"       Your final hand: {player_cards}, final score: {player_result}")
          print(f"       Computer's final hand: {computer_cards}, final score: {computer_result}")
          print("You went over. You lose")
          return False
     else:
          return True

def deal_cards(getCard):
    sum = 0
    computer_sum = 0
    computer_choice = random.choice(computer_choice_list)


    if getCard == 'y':  
       player_cards.append(pick_card())
    
    if computer_choice == 'y':
        computer_cards.append(pick_card())
    
    for card in player_cards:
        sum += card
    for com in computer_cards:
        computer_sum += com
    print(f"  Your cards: {player_cards}, current score: {sum}")
    # print(f"computer's card {computer_cards}")
    print(f"  Computer's first card: {computer_cards[0]}")

    if getCard == 'y':
       return winner_func(sum, computer_sum)
    else:
       return winner_func(sum, computer_sum)

should_continue = deal_cards(getCard)

while should_continue:
     get_card = input("Type 'y' to get another card, type 'n' to pass: ")
     if get_card == 'y':
         should_continue = deal_cards(get_card)
     else:
         should_continue = deal_cards(getCard='n')

print()
print()
play_again = input("Do you want to play the blackjack game again? type 'y' to play, otherwise 'n' to exit: ")
while play_again == 'y':
    print(logo)
    player_cards = []
    computer_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def pick_card(cards = cards):
        """Fuction to choose random card"""
        return random.choice(cards)

    player_cards.append(pick_card())
    computer_cards.append(pick_card())
    should_play = input("Do you want to play the blackjack game? Type 'y' to play 'n' for no: ")
    computer_first_card = computer_cards[0]

    getCard='y'
    computer_choice_list = ['y', 'n']

    should_continue = deal_cards(getCard)

    while should_continue:
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card == 'y':
             should_continue = deal_cards(get_card)
        else:
             should_continue = deal_cards(getCard='n')

    play_again = input("Do you waant to play the blackjack again? type 'y' to play, otherwise 'n' to exit: ")

print("Goodbye!!!")