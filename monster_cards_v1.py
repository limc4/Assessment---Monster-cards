"""Monster Cards - v1
Program to store monster cards and allow user to interact with cards
Dictionary of monster cards, main function, and function to output all cards
Created by Charlotte Lim"""

import easygui

deck = \
    {
        "Stoneling": {
            "Strength": 7,
            "Speed": 1,
            "Stealth": 25,
            "Cunning": 15
        },
        "Vexscream": {
            "Strength": 1,
            "Speed": 6,
            "Stealth": 21,
            "Cunning": 19
        },
        "Dawnmirage": {
            "Strength": 5,
            "Speed": 15,
            "Stealth": 18,
            "Cunning": 22
        },
        "Blazegolem": {
            "Strength": 15,
            "Speed": 20,
            "Stealth": 23,
            "Cunning": 6
        },
        "Websnake": {
            "Strength": 7,
            "Speed": 15,
            "Stealth": 10,
            "Cunning": 5
        },
        "Moldvine": {
            "Strength": 21,
            "Speed": 18,
            "Stealth": 14,
            "Cunning": 5
        },
        "Vortexwing": {
            "Strength": 19,
            "Speed": 13,
            "Stealth": 19,
            "Cunning": 2
        },
        "Rotthing": {
            "Strength": 16,
            "Speed": 7,
            "Stealth": 4,
            "Cunning": 12
        },
        "Froststep": {
            "Strength":14,
            "Speed": 14,
            "Stealth": 17,
            "Cunning": 4
        },
        "Wispghoul": {
            "Strength": 17,
            "Speed": 19,
            "Stealth": 3,
            "Cunning": 2
        },

}

def output_all():
    """Function to output all cards in monster cards deck into Python console"""
    all_cards = "========[ Monster cards in the deck ]========\n"
    for card, card_info in deck.items():
        all_cards += f"\n--------{card} Card--------\n"
        for key in card_info:
            all_cards += f"{key}: {card_info[key]}\n"
    print(all_cards)


def main_routine():
    """Function to run main routine"""
    while True:
        choice = easygui.buttonbox("What would you like to do?",
                                   "Actions",
                                   choices=["Output all cards",
                                            "Quit"])
        if choice == "Output all cards":
            output_all()
        else:
            quit()

# Main routine
main_routine()
