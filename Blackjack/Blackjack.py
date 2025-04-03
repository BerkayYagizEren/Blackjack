# Blackjack Game

import random

# Print welcome message
print('Welcome to the Bora\'s BlackJack. I hope you believe in your chance')


# Display cards function
def show_all_cards(liste):
    for i in liste:
        print(i, end=' ')
    print()


# Card drawing function
def pick_a_card(liste):
    the_card = random.choice(liste)
    liste.remove(the_card)
    return the_card


# Hand value calculation (with Ace handling)
def alternative_sum(liste):
    if sum(liste) <= 21:
        return sum(liste)
    elif sum(liste) > 21 and 11 in liste:  # Convert Ace 11→1 if bust
        liste[liste.index(11)] = 1
        return sum(liste)
    return sum(liste)


# Main game loop
while True:
    # Initialize hands
    your_cards = []
    computer_cards = []

    # Create deck (4 suits × 2-11 + 8 face cards)
    cards = [i for i in range(2, 12)] * 4 + [10] * 8

    # Deal initial cards
    for _ in range(2):
        your_cards.append(pick_a_card(cards))
        computer_cards.append(pick_a_card(cards))

    # Player turn
    while alternative_sum(your_cards) < 21:
        print('Your cards:')
        show_all_cards(your_cards)
        print(f'Computer shows: {computer_cards[0]}')

        # Hit or stand
        if input('Hit? (Y/N): ').upper() != 'Y':
            break
        your_cards.append(pick_a_card(cards))

    # Computer turn (hits until 16+)
    while alternative_sum(computer_cards) < 16 and alternative_sum(your_cards) <= 21:
        computer_cards.append(pick_a_card(cards))

    # Show final hands
    print('Your cards:', end=' ')
    show_all_cards(your_cards)
    print('Computer cards:', end=' ')
    show_all_cards(computer_cards)

    # Determine winner
    your_sum = alternative_sum(your_cards)
    comp_sum = alternative_sum(computer_cards)

    if (your_sum > comp_sum and your_sum <= 21) or comp_sum > 21:
        print('You win!')
    elif your_sum == comp_sum:
        print('Draw')
    else:
        print('You lost')

    # Play again?
    if input('Play again? (Y/N): ').upper() != 'Y':
        break