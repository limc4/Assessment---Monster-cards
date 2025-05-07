"""Monster Cards - v4
Program to store monster cards and allow user to interact with cards
function to delete existing monster card from catalogue added
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
    cards = [] # to store all cards in catalogue

    # appends all cards in catalogue to cards
    for card in catalogue:
        cards.append(card)

    print_card = "" # string to store card details

    # allows the user to find and choose card from catalogue
    find = easygui.choicebox("What is the name of the card you would like to find?",
                             "Find a card",
                             choices = cards)

    # adds and formats details in print_card string
    for card, card_info in catalogue.items():
        if card == find:
            print_card += f"\n--------[ {find} Card ]--------\n"
            for key in card_info:
                print_card += f"{key}: {card_info[key]}\n"

    return print_card

def add_card():
    name = easygui.enterbox("What is the name of this monster?",
                            "Monster name").title()

    strength = easygui.integerbox(f"What is {name}'s strength level?"
                                  f"\n\nEnter a number from 1 to 25",
                                  "Strength level",
                                  "",1, 25)

    speed = easygui.integerbox(f"What is {name}'s speed level?"
                                  f"\n\nEnter a number from 1 to 25",
                                  "Speed level",
                                  "", 1, 25)

    stealth = easygui.integerbox(f"What is {name}'s stealth level?"
                                  f"\nEnter a number from 1 to 25",
                                  "Stealth level",
                                  "", 1, 25)

    cunning = easygui.integerbox(f"What is {name}'s cunning level?"
                                  f"\nEnter a number from 1 to 25",
                                  "Cunning level",
                                  "", 1, 25)

    new_monster = {
        "Strength": strength,
        "Speed": speed,
        "Stealth": stealth,
        "Cunning": cunning
    }

    catalogue[name] = new_monster

    print_card = ""
    for card, card_info in catalogue.items():
        if card == name:
            print_card += f"\n--------[ {name} Card ]--------\n"
            for key in card_info:
                print_card += f"{key}: {card_info[key]}\n"

    return print_card

def delete_card():
    cards_list = []  # to store all cards in catalogue
    cards_string = "----[ Monster cards in deck: ]----"
    output = ""

    # appends all cards in catalogue to cards
    for card in catalogue:
        cards_list.append(card)

    # for loop to add each card to all_cards string
    for card in cards_list:
        cards_string += f"\n        {card}"

    del_card = ""
    if catalogue == {}:
        output = "The catalogue is empty"
    else:
        while not del_card:
            # allows the user to find and choose card from catalogue
            del_card = easygui.choicebox(f"What is the name of the card you "
                                         f"would like to delete?",
                                    "Which card to delete?",
                                         choices = cards_list).title()

        if del_card in catalogue:
            output = f"{del_card} Card found and deleted."
            del catalogue[del_card]
            output += ("\n\nThe updated catalogue has been printed in the "
                       f"Python Console.")
        elif del_card not in catalogue:
            output = f"{del_card} Card does not exist\n\n"

    output_all()

    return output

def main_routine():
    """Function to run main routine"""
    while True: # while loop to allow the user to keep making choices unless
                # user quits the program

        # buttonbox used to limit errors
        choice = easygui.buttonbox("What would you like to do?",
                                   "Actions",
                                   choices=["Output all cards",
                                            "Search for existing card",
                                            "Add a new card",
                                            "Delete existing card",
                                            "Quit"])
        if choice == "Output all cards":
            output_all() # calls the function to output all cards in catalogue

        elif choice == "Search for existing card":
            # calls the function to find an existing card and outputs the details
            easygui.msgbox(find_card(), "Card info")
        elif choice == "Add a new card":
            easygui.msgbox(add_card(), "Add a new card")
        elif choice == "Delete existing card":
            easygui.msgbox(delete_card(), "Delete a card")
        else:
            quit() # quits the entire program

# Main routine
main_routine()
