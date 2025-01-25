import tkinter as tk
from enum import IntEnum
import random

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors Lizard Spock")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select an action:")
        self.label.pack()

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play(Action.Rock))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play(Action.Paper))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play(Action.Scissors))
        self.scissors_button.pack()

        self.lizard_button = tk.Button(self.root, text="Lizard", command=lambda: self.play(Action.Lizard))
        self.lizard_button.pack()

        self.spock_button = tk.Button(self.root, text="Spock", command=lambda: self.play(Action.Spock))
        self.spock_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def play(self, user_action):
        computer_action = random.choice(list(Action))
        defeats = victories[user_action]
        if user_action == computer_action:
            result = f"Both players selected {user_action.name}. It's a tie!"
        elif computer_action in defeats:
            result = f"{user_action.name} beats {computer_action.name}! You win!"
        else:
            result = f"{computer_action.name} beats {user_action.name}! You lose."

        self.result_label['text'] = result

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()