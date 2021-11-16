'''This module represents the code for the BlackJack game.'''
from random import randint
from deck import card_name, card_value, end_turn_status, end_game_status

def draw_card():
    '''This here defines the function for the random card to be drawn.'''
    card = randint(1, 13)
    print('Drew a ' + card_name(card))
    return card

def main():
    '''The code for the BlackJack game proper'''

    print("-----------")
    print("YOUR TURN")
    print("-----------")

    user_hand = 0
    drawn_count = 0
    hit = True
    while hit:
        card_drawn = draw_card()

        user_hand += card_value(card_drawn)
        drawn_count += 1

        if user_hand >= 21:
            hit = False
        elif drawn_count >= 2:
            hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y'

    print('Final hand: ' + str(user_hand) + '.')
    #To avoid extra spaces, it prints the end status of the player hand only when it's 21 and above.
    if user_hand >= 21:
        print(end_turn_status(user_hand))

    print("-----------")
    print("DEALER TURN")
    print("-----------")

    dealer_hand = 0
    drawn_count = 0

    while dealer_hand <= 17:
        if drawn_count >= 2:
            print('Dealer has ' + str(dealer_hand) + '.')

        card_drawn = draw_card()
        dealer_hand += card_value(card_drawn)
        drawn_count += 1

    print('Final hand: ' + str(dealer_hand) + '.')
    #To avoid extra spaces, it prints the end status of the player hand only when it's 21 and above.
    if dealer_hand >= 21:
        print(end_turn_status(dealer_hand))

    print("-----------")
    print("GAME RESULT")
    print("-----------")

    print(end_game_status(user_hand, dealer_hand))

if __name__ == "__main__":
    main()
