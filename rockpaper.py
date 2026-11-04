import random
import tkinter as tk

def play_game(player_choice):
    # Get computer's choice
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
        
    # Build and show the summary text
    summary = "Your Choice: " + player_choice + "\n"
    summary = summary + "Computer's Choice: " + computer_choice + "\n\n"
    summary = summary + "Result: " + result
    
    result_label.config(text=summary)

# --- GUI Window Setup ---
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")

title_label = tk.Label(window, text="Rock Paper Scissors Game", font=("Arial", 18))
title_label.pack(pady=10)

instruction_label = tk.Label(window, text="Click a button to make your move:", font=("Arial", 12))
instruction_label.pack(pady=10)

# --- Action Buttons ---
rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play_game("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play_game("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)

# --- Game Output ---
result_label = tk.Label(window, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

window.mainloop()
