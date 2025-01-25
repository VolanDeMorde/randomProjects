# Rock Paper Scissors Lizard Spock game

import random
from enum import IntEnum

class Action(IntEnum):
    # Define the possible actions in the game using an enumeration
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

# Define the winning combinations for each action
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def get_user_selection():
    """
    Prompt the user to make a selection and return the corresponding Action.
    """
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        print("Invalid selection. Enter a value in range [0, 4]")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    if input("Play again? (y/n): ").lower() != "y":
        break