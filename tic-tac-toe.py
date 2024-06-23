import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='normal 20 bold', height=3, width=6,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg='blue' if self.current_player == 'X' else 'green')
            if self.check_winner():
                self.highlight_winner()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        self.win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                               (0, 3, 6), (1, 4, 7), (2, 5, 8),
                               (0, 4, 8), (2, 4, 6)]
        for a, b, c in self.win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                self.winning_combination = (a, b, c)
                return True
        return False

    def highlight_winner(self):
        for index in self.winning_combination:
            self.buttons[index].config(bg='yellow')

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ', bg='SystemButtonFace')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
