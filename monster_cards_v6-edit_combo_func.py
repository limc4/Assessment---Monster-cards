"""Monster Cards - v6 - edit combo function

Program to store monster cards and allow user to interact with cards.

Created by Charlotte Lim.
"""

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
            "Strength": 14,
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
    console.
    """
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
    return card information.
    """
    cards = []  # to store all cards in catalogue

    # appends all cards in catalogue to cards
    for card in catalogue:
        cards.append(card)

    print_card = ""  # string to store card details

    # allows the user to find and choose card from catalogue
    find = easygui.choicebox("What is the name of the card you would "
                             "like to find?",
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
    """Function to allow user to add a new monster card to the catalogue and
    return new card details.
    """
    # allows user to input the name of their new monster card
    name = easygui.enterbox("What is the name of this monster?",
                            "Monster name").title()

    # allows user to input the strength level of their new monster card
    # (from 1-25)
    strength = easygui.integerbox(f"What is {name}'s strength level?"
                                  f"\n\nEnter a number from 1 to 25",
                                  "Strength level",
                                  "", 1, 25)

    # allows user to input the speed level of their new monster card
    # (from 1-25)
    speed = easygui.integerbox(f"What is {name}'s speed level?"
                                  f"\n\nEnter a number from 1 to 25",
                                  "Speed level",
                                  "", 1, 25)

    # allows user to input the stealth level of their new monster card
    # (from 1-25)
    stealth = easygui.integerbox(f"What is {name}'s stealth level?"
                                  f"\nEnter a number from 1 to 25",
                                  "Stealth level",
                                  "", 1, 25)

    # allows user to input the cunning level of their new monster card
    # (from 1-25)
    cunning = easygui.integerbox(f"What is {name}'s cunning level?"
                                  f"\nEnter a number from 1 to 25",
                                  "Cunning level",
                                  "", 1, 25)

    # formats all inputted information into a new dictionary
    new_monster = {
        "Strength": strength,
        "Speed": speed,
        "Stealth": stealth,
        "Cunning": cunning
    }

    # saves new monster card in catalogue
    catalogue[name] = new_monster

    # allows user to see new card details
    print_card = ""
    for card, card_info in catalogue.items():
        if card == name:
            print_card += f"\n--------[ {name} Card ]--------\n"
            for key in card_info:
                print_card += f"{key}: {card_info[key]}\n"

    return print_card


def delete_card():
    """Function to allow user to delete a card from catalogue and print
    updated catalogue into the Python console.
    """
    cards_list = []  # to store all cards in catalogue
    cards_string = "----[ Monster cards in deck: ]----"
    output = ""

    # appends all cards in catalogue to cards
    for card in catalogue:
        cards_list.append(card)

    # for loop to add each card to all_cards string
    for card in cards_list:
        cards_string += f"\n        {card}"

    if catalogue == {}:  # no cards to delete if the catalogue is empty
        output = "The catalogue is empty.\n\nThere are no cards to delete"
    else:
        # allows the user to find and choose card from catalogue
        del_card = easygui.choicebox(f"What is the name of the card you "
                                     f"would like to delete?",
                                    "Which card to delete?",
                                     choices = cards_list)

        # checks if del_card is in catalogue and outputs updated catalogue
        if del_card in catalogue:
            output = f"{del_card} Card found and deleted."
            del catalogue[del_card]
            output += ("\n\nThe updated catalogue has been printed in the "
                       "Python Console.")

        elif del_card not in catalogue:
            output = f"{del_card} Card does not exist\n\n"

    output_all()

    return output

def edit_card():
    card_names = list(catalogue.keys())
    searched_card = easygui.choicebox("What card are you looking for?",
                                           "Which card", card_names)

    if searched_card is None:
        return "Card selection cancelled!"

    searched_card_info = catalogue[searched_card]
    skills = list(searched_card_info.keys())

    confirm_edit = "Keep editing"
    while confirm_edit == "Keep editing":
        # shows the current card before the user chooses what to modify
        display_card_info = f"\n--------[ {searched_card} Card ]--------\n"
        for skill, value in searched_card_info.items():
            display_card_info += f"{skill}: {value}\n"

        item_modify = easygui.buttonbox(
            f"{display_card_info}\n\n"  
            f"Which part would you like to modify?",
            "Edit card",
            choices = skills)

        if item_modify is None:
            break

        new_detail = easygui.integerbox(
            f"What would you like to change the {item_modify} to?",
            f"{item_modify} change",
            searched_card_info[item_modify],
            1,
            25
        )

        if new_detail is None:
            break

        searched_card_info[
            item_modify] = new_detail  # changes detail to what user inputted

        # shows the user what the updated info looks like
        updated_card_info = f"\n--------[ {searched_card} Card ]--------\n"
        for skill, value in searched_card_info.items():
            updated_card_info += f"{skill}: {value}\n"

        confirm_edit = easygui.buttonbox(
            f"{updated_card_info}\n\n"  
            f"Confirm changes:",
            "Confirm changes?",
            ["Confirm", "Keep editing", "Cancel"])

        if confirm_edit == "Confirm":  # confirms the changes
            catalogue[searched_card] = searched_card_info
            return f"{searched_card} updated successfully!"
        elif confirm_edit == "Cancel":  # cancels the changes
            return f"Edit for {searched_card} cancelled!"

    return f"Edit for {searched_card} cancelled!"

def main_routine():
    """Function to run main routine."""
    while True:  # while loop allows the user to keep making choices unless
                 # user quits the program

        # buttonbox used to limit errors
        choice = easygui.buttonbox("What would you like to do?",
                                   "Actions",
                                   choices=["Output all cards",
                                            "Search for existing card",
                                            "Add a new card",
                                            "Delete existing card",
                                            "Edit a card from the catalogue",
                                            "Quit"])

        if choice == "Output all cards":
            # calls the function to output all cards in catalogue
            output_all()

        elif choice == "Search for existing card":
            # calls the function to find an existing card and outputs the
            # details
            easygui.msgbox(find_card(), "Card info")

        elif choice == "Add a new card":
            # calls the function to add a new card to the catalogue
            easygui.msgbox(add_card(), "Add a new card")

        elif choice == "Delete existing card":
            # calls the function to delete existing card from the catalogue
            easygui.msgbox(delete_card(), "Delete a card")

        elif choice == "Edit a card from the catalogue":
            easygui.msgbox(edit_card())
            print("Updated Catalogue:")
            output_all()

        else:
            quit()  # quits the entire program


# Main routine
main_routine()
