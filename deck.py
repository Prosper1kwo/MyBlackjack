'''The purpose of this module is to define the functions used in the blackjack game.'''

def card_name(card_rank):
    '''This function returns the official name of each card drawn.

    Args:
        card_rank: The numerical representation of the card.

    Returns:
        The official name of the card is returned as a string.

    Examples:
        card_name(1) returns "Ace"
        card_name(5) returns "5"
        card_name(13) returns "King"
    '''

    if card_rank == 1:
        name = "Ace"
    elif 2 <= card_rank <= 10:
        name = str(card_rank)
    elif card_rank == 11:
        name = "Jack"
    elif card_rank == 12:
        name = "Queen"
    elif card_rank == 13:
        name = "King"

    return name

def card_value(card_rank):
    '''This function will return the numerical value of each card drawn.

    Args:
        card_rank: The numerical representation of the card.

    Returns:
        Returns in int, the numerical value.

    Examples:
        card_value(1) returns 11
        card_value(4) returns 4
        card_value() returns 10 for face cards
    '''
    if card_rank == 1:
        value = 11
    elif 2 <= card_rank <= 10:
        value = card_rank
    elif card_rank == 11:
        value = 10
    elif card_rank == 12:
        value = 10
    elif card_rank == 13:
        value = 10

    return value

def end_turn_status(hand):
    '''This returns the status of the game at the end of each player's turn

    Args:
        hand: The sum of all the cards drawn by a player.

    Returns:
        Returns the status of the game depending on the hand.

    Examples:
        end_turn_status(15) returns ""
        end_turn_status(21) returns "BLACKJACK!"
        end_turn_status(24) returns "BUST."
    '''
    if hand == 21:
        turn_status = "BLACKJACK!"
    elif hand < 21:
        turn_status = ""
    elif hand > 21:
        turn_status = "BUST."

    return turn_status

def end_game_status(user_hand, dealer_hand):
    '''This reveals the winner based on the final hands.

    Args:
        user_hand: The sum of all the user's drawn cards
        dealer_hand: The sum of all the dealer's drawn cards

    Returns:
        Returns the printed statement of the winner as a string.

    Examples:
        end_game_status(20,21) returns "Dealer wins!"
        end_game_status(21,25) returns "You win!"
        end_game_status(20,20) returns "Tie."
    '''
    if user_hand == dealer_hand:
        game_status = "Tie."
    elif user_hand != 21 and dealer_hand == 21:
        game_status = "Dealer wins!"
    elif user_hand == 21 and dealer_hand != 21:
        game_status = "You win!"
    elif user_hand < dealer_hand < 21:
        game_status = "Dealer wins!"
    elif dealer_hand < user_hand < 21:
        game_status = "You win!"
    elif user_hand > 21 and dealer_hand > 21:
        game_status = "Tie."
    elif user_hand < 21 < dealer_hand:
        game_status = "You win!"
    elif dealer_hand < 21 < user_hand:
        game_status = "Dealer wins!"

    return game_status

