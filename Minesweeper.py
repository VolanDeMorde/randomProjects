import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, width=10, height=10, num_mines=10):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flagged = [[False for _ in range(width)] for _ in range(height)]
        self.mines = set()
        self.game_over = False
        
        # Initialize game
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))
                mines_placed += 1

    def calculate_numbers(self):
        for (x, y) in self.mines:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if (nx, ny) not in self.mines:
                            self.board[ny][nx] += 1

    def reveal(self, x, y):
        if self.flagged[y][x] or self.revealed[y][x]:
            return
            
        if (x, y) in self.mines:
            self.game_over = True
            return
            
        self.revealed[y][x] = True
        
        if self.board[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (x, y) not in self.mines:
                    return False
        return True

class MinesweeperGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        
        self.buttons = []
        # Define colors as an instance variable
        self.colors = {
            1: "blue",
            2: "green",
            3: "red",
            4: "purple",
            5: "maroon",
            6: "turquoise",
            7: "black",
            8: "gray"
        }
        
        for y in range(game.height):
            row = []
            for x in range(game.width):
                btn = tk.Button(self.root, width=2, height=1, font=('Arial', 12),
                              relief='raised', bg='lightgray')
                btn.grid(row=y, column=x)
                btn.bind('<Button-1>', lambda e, x=x, y=y: self.reveal(x, y))
                btn.bind('<Button-3>', lambda e, x=x, y=y: self.toggle_flag(x, y))
                row.append(btn)
            self.buttons.append(row)
        
        self.update_ui()

    def reveal(self, x, y):
        if self.game.game_over or self.game.flagged[y][x]:
            return
            
        self.game.reveal(x, y)
        
        if self.game.game_over:
            self.show_all_mines()
            self.update_ui()
            messagebox.showinfo("Game Over", "You hit a mine!")
            self.root.destroy()
            return
            
        if self.game.check_win():
            self.update_ui()
            messagebox.showinfo("Congratulations!", "You've won!")
            self.root.destroy()
            return
            
        self.update_ui()

    def toggle_flag(self, x, y):
        if not self.game.revealed[y][x] and not self.game.game_over:
            self.game.flagged[y][x] = not self.game.flagged[y][x]
            self.update_ui()

    def update_ui(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                btn = self.buttons[y][x]
                if self.game.revealed[y][x]:
                    btn.config(relief='sunken', bg='white')
                    if (x, y) in self.game.mines:
                        btn.config(text='💣', bg='red')
                    else:
                        count = self.game.board[y][x]
                        btn.config(text=str(count) if count > 0 else '',
                                 fg=self.colors.get(count, "black"))  # Use self.colors
                elif self.game.flagged[y][x]:
                    btn.config(text='🚩', bg='lightgray')
                else:
                    btn.config(text='', bg='lightgray')

    def show_all_mines(self):
        for x in range(self.game.width):
            for y in range(self.game.height):
                if (x, y) in self.game.mines:
                    self.buttons[y][x].config(text='💣', bg='red')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Minesweeper(10, 10, 10)
    gui = MinesweeperGUI(game)
    gui.run()