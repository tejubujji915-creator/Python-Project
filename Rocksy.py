
"""
Rock Paper Scissors - GUI Game
Run this file to open a window and play against the computer.
"""

import tkinter as tk
import random

CHOICES = ["Rock", "Paper", "Scissors"]
EMOJI = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("420x400")
        self.root.resizable(True, True)

        self.player_score = 0
        self.computer_score = 0

        # Title
        tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold")).pack(pady=15)

        # Score display
        self.score_label = tk.Label(root, text=self.score_text(), font=("Helvetica", 14))
        self.score_label.pack(pady=5)

        # Result display
        self.result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 14), wraplength=380)
        self.result_label.pack(pady=15)

        # Choices display
        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(pady=10)

        self.player_choice_label = tk.Label(self.choices_frame, text="", font=("Helvetica", 40))
        self.player_choice_label.grid(row=0, column=0, padx=30)

        self.vs_label = tk.Label(self.choices_frame, text="VS", font=("Helvetica", 16, "bold"))
        self.vs_label.grid(row=0, column=1)

        self.computer_choice_label = tk.Label(self.choices_frame, text="", font=("Helvetica", 40))
        self.computer_choice_label.grid(row=0, column=2, padx=30)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=25)

        for choice in CHOICES:
            btn = tk.Button(
                button_frame,
                text=f"{EMOJI[choice]} {choice}",
                font=("Helvetica", 12),
                width=10,
                command=lambda c=choice: self.play(c)
            )
            btn.pack(side=tk.LEFT, padx=8)

        # Reset button
        tk.Button(root, text="Reset Score", font=("Helvetica", 10), command=self.reset_score).pack(pady=10)

    def score_text(self):
        return f"You: {self.player_score}    Computer: {self.computer_score}"

    def play(self, player_choice):
        computer_choice = random.choice(CHOICES)

        self.player_choice_label.config(text=EMOJI[player_choice])
        self.computer_choice_label.config(text=EMOJI[computer_choice])

        result = self.get_result(player_choice, computer_choice)

        if result == "win":
            self.player_score += 1
            self.result_label.config(text=f"You win! {player_choice} beats {computer_choice}", fg="green")
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(text=f"You lose! {computer_choice} beats {player_choice}", fg="red")
        else:
            self.result_label.config(text=f"It's a tie! Both chose {player_choice}", fg="black")

        self.score_label.config(text=self.score_text())

    def get_result(self, player, computer):
        if player == computer:
            return "tie"
        beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        if beats[player] == computer:
            return "win"
        return "lose"

    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=self.score_text())
        self.result_label.config(text="Score reset. Make your move!", fg="black")
        self.player_choice_label.config(text="")
        self.computer_choice_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()