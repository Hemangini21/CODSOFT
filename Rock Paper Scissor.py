import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score, points_to_win

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    if user_score == points_to_win:
        messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        reset_game()
    elif computer_score == points_to_win:
        messagebox.showinfo("Game Over", "Sorry! Computer won the game!")
        reset_game()

    messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

# Function to reset the game
def reset_game():
    global user_score, computer_score, points_to_win
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    start_button.config(state=tk.NORMAL)
    rock_btn.config(state=tk.DISABLED)
    paper_btn.config(state=tk.DISABLED)
    scissors_btn.config(state=tk.DISABLED)
    points_entry.delete(0, tk.END)
    points_entry.focus()

# Function to handle button clicks
def play(choice):
    determine_winner(choice)

# Function to start the game
def start_game():
    global points_to_win
    points_to_win = int(points_entry.get())
    if points_to_win <= 0:
        messagebox.showerror("Error", "Please enter a valid number of points greater than zero.")
    else:
        start_button.config(state=tk.DISABLED)
        rock_btn.config(state=tk.NORMAL)
        paper_btn.config(state=tk.NORMAL)
        scissors_btn.config(state=tk.NORMAL)

# Initialize scores
user_score = 0
computer_score = 0

# Create a window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="#e0e0e0")

# Create labels for scores
user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Arial', 14, 'bold'), bg="#e0e0e0", fg="#333333")
user_score_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Arial', 14, 'bold'), bg="#e0e0e0", fg="#333333")
computer_score_label.grid(row=0, column=2, columnspan=2, padx=10, pady=5)

# Create entry widget for points to win
points_entry_label = tk.Label(root, text="Points to Win:", font=('Arial', 12), bg="#e0e0e0", fg="#333333")
points_entry_label.grid(row=1, column=0, padx=10, pady=5)
points_entry = tk.Entry(root, font=('Arial', 12), bg="#ffffff", fg="#333333")
points_entry.grid(row=1, column=1, padx=10, pady=5)

# Create start button
start_button = tk.Button(root, text="Start", font=('Arial', 12), padx=10, pady=5, command=start_game, bg="#4CAF50", fg="white")
start_button.grid(row=1, column=2, padx=10, pady=5)

# Create reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 12), padx=10, pady=5, command=reset_game, bg="#f44336", fg="white")
reset_button.grid(row=1, column=3, padx=10, pady=5)

# Create buttons for Rock, Paper, and Scissors
rock_btn = tk.Button(root, text="Rock", font=('Arial', 12), padx=10, pady=5, command=lambda: play("Rock"), state=tk.DISABLED, bg="#2196F3", fg="white")
rock_btn.grid(row=2, column=0, padx=10, pady=5)
paper_btn = tk.Button(root, text="Paper", font=('Arial', 12), padx=10, pady=5, command=lambda: play("Paper"), state=tk.DISABLED, bg="#2196F3", fg="white")
paper_btn.grid(row=2, column=1, padx=10, pady=5)
scissors_btn = tk.Button(root, text="Scissors", font=('Arial', 12), padx=10, pady=5, command=lambda: play("Scissors"), state=tk.DISABLED, bg="#2196F3", fg="white")
scissors_btn.grid(row=2, column=2, padx=10, pady=5)

# Run the application
root.mainloop()
