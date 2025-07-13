"""Monster Cards - v6ii - edit combo function

Program to store monster cards and allow user to edit cards - test

Created by Charlotte Lim.
"""

import easygui
import copy

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


def edit_card():
    card_names = list(catalogue.keys())
    searched_card = easygui.choicebox("What card are you looking for?",
                                           "Which card", card_names)

    if searched_card is None:
        return "Card selection cancelled!"

    original_card_name = searched_card
    modified_card_info = copy.deepcopy(catalogue[original_card_name])
    current_display_name = original_card_name

    confirm_edit = "Keep editing"
    while confirm_edit == "Keep editing":
        # shows the current card before the user chooses what to modify
        temp_card_display_for_choice = f"\n--------[ {current_display_name} Card ]--------\n"
        temp_card_display_for_choice += f"Name: {current_display_name}\n"

        # get fresh skills list as a precaution, though it typically won't change
        skills = list(modified_card_info.keys())
        for skill, value in modified_card_info.items():
            temp_card_display_for_choice += f"{skill}: {value}\n"

        modification_choices = ["Name"] + skills

        item_modify = easygui.buttonbox(f"{temp_card_display_for_choice}\n\n"
                                        f"Which part would you like to modify?",
                                        "Edit card",
                                        choices = modification_choices)

        if item_modify is None:
            return "Edit cancelled!"

        if item_modify == "Name":
            new_name = easygui.enterbox(
                f"What would you like to change the card name to?",
                "Change Card Name",
                current_display_name).title()

            if new_name is None:
                continue

            new_name = new_name.strip()

            if not new_name:
                easygui.msgbox("Card name cannot be empty. Please try again.",
                               "Error")
                continue

            if new_name == current_display_name:
                easygui.msgbox("Card name is the same. No change applied.",
                               "Info")
                continue

            # Check for duplicate names only if the new name is different from the original name
            # AND if it actually exists in the catalogue. This prevents flagging the original name
            # as a duplicate if only skills are modified.
            if new_name in catalogue and new_name != original_card_name:
                easygui.msgbox(
                    f"A card with the name '{new_name}' already exists. Please choose a different name.",
                    "Duplicate Name Error")
                continue

            current_display_name = new_name
            easygui.msgbox(
                f"Card name changed to '{current_display_name}' for this session.",
                "Name Updated (Pending Confirmation)")

        else:  # It's a skill to modify
            new_detail = easygui.integerbox(
                f"What would you like to change the {item_modify} to?",
                f"{item_modify} change",
                modified_card_info[item_modify],
                1,
                25
            )

            if new_detail is None:
                continue

            modified_card_info[item_modify] = new_detail

        # ensures the confirmation screen shows the immediate update
        # (put before confirm_edit screen)
        show_updated_card_for_confirm = f"\n--------[ {current_display_name} Card ]--------\n"
        show_updated_card_for_confirm += f"Name: {current_display_name}\n"
        for skill, value in modified_card_info.items():
            show_updated_card_for_confirm += f"{skill}: {value}\n"

        confirm_edit = easygui.buttonbox(
            f"{show_updated_card_for_confirm}\n\n"
            f"Confirm changes:",
            "Confirm changes?",
            ["Confirm", "Keep editing", "Cancel"])

        if confirm_edit == "Confirm":
            if original_card_name != current_display_name:
                del catalogue[original_card_name]
                catalogue[current_display_name] = modified_card_info
            else:
                # if only skills were changed (or nothing), updates the existing reference
                # important because 'modified_card_data' is a deep copy
                # if only skills changed, puts the modified deep copy back
                catalogue[original_card_name] = modified_card_info

            return f"{current_display_name} updated successfully!"

        elif confirm_edit == "Cancel":
            return "Edit cancelled!"

    return "Edit cancelled!"


# --- Calling the function and displaying results ---
status_message = edit_card()

easygui.msgbox(status_message, "Edit Status")

print("\n--- Current Monster Catalogue (Console Output) ---")
for card_name, details in catalogue.items():
    print(f"--------[ {card_name} ]--------")
    for skill, value in details.items():
        print(f"{skill}: {value}")
    print()