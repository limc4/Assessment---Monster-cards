"""Monster Cards - v2
Program to store monster cards and allow user to interact with cards
function to search for a card added (trial a)
Created by Charlotte Lim"""

import easygui

# multidimensional dictionary containing monster cards
catalogue = \
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
    """Function to output all cards in monster cards catalogue into Python
    console"""

    # heading for output
    all_cards = "========[ Monster cards in the deck ]========\n"

    # for loop to add each card to all_cards string
    for card, card_info in catalogue.items():
        all_cards += f"\n--------{card} Card--------\n"
        for key in card_info:
            all_cards += f"{key}: {card_info[key]}\n"

    print(all_cards)

def find_card():
    """Function to allow user to search for existing card in the catalogue and
    return card information"""
    cards_list = [] # to store all cards in catalogue
    cards_string = "----[ Monster cards in deck: ]----"

    # appends all cards in catalogue to cards
    for card in catalogue:
        cards_list.append(card)

    print_card = "" # string to store card details

    # for loop to add each card to all_cards string
    for card in cards_list:
        cards_string += f"\n        {card}"

    find = ""
    while not find:
        # allows the user to find and choose card from catalogue
        find = easygui.enterbox(f"{cards_string}\n"
                                f"\nWhat is the name of the card you would "
                                f"like to see the details of?",
                                 "Find a card").title()

        # adds and formats details in print_card string
        for card, card_info in catalogue.items():
            if card == find:
                print_card += f"\n--------[ {find} Card ]--------\n"
                for key in card_info:
                    print_card += f"{key}: {card_info[key]}\n"

        # if user input is not applicable, user gets another chance to enter
        # correct card
        if find not in cards_list:
            easygui.msgbox("The card you have entered does not exist."
                        "\nPlease read the list carefully, check the spelling,"
                           " and try again",
                           "Card not found")
            find = ""

    return print_card

def main_routine():
    """Function to run main routine"""
    while True: # while loop to allow the user to keep making choices unless
                # user quits the program

        # buttonbox used to limit errors
        choice = easygui.buttonbox("What would you like to do?",
                                   "Actions",
                                   choices=["Output all cards",
                                            "Search for existing card",
                                            "Quit"])
        if choice == "Output all cards":
            output_all() # calls the function to output all cards in catalogue

        elif choice == "Search for existing card":
            # calls the function to find an existing card and outputs the details
            easygui.msgbox(find_card(), "Card info")
        else:
            quit() # quits the entire program

# Main routine
main_routine()
