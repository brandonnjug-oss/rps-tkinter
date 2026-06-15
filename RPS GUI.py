import tkinter as tk
from tkinter import ttk
import random

# Window setup
root = tk.Tk()
root.title("RPS")
root.geometry("375x280")

# StringVars for dynamic label text
choicePlayerMove = tk.StringVar()         # Holds the player's selected move from the dropdown
showComputerMove = tk.StringVar()         # Displayed computer move label text
showComputerMove.set(' Computer Move: ') # Default before any game is played
showResult = tk.StringVar()              # Displayed result (Win/Loss/Draw)
showResult.set('')

# Title label
title = tk.Label(root, text=" Rock, Paper, Scissors", font=("Segoe UI", 25, 'bold'))
title.pack(pady=10)

# Move selection row
slctFrame = tk.Frame(root)
slctFrame.pack(anchor="w", pady=10)

slctMve = tk.Label(slctFrame, text=" Select Move: ", font=("Segoe UI", 14))
slctMve.pack(side="left", pady=10)

def on_dropdown_change(event):
    """Reset the UI when the player selects a new move."""
    showComputerMove.set(' Computer Move: ')  # Clear previous computer move
    showResult.set('')                         # Clear previous result
    button.config(state="normal")             # Enable the Confirm button
    button.config(bg="#00a600")               # Change button colour to green (ready state)

# Dropdown for move selection; readonly prevents typing arbitrary values
slctDrpdwn = ttk.Combobox(
    slctFrame,
    textvariable=choicePlayerMove,
    values=["Rock", "Paper", "Scissors"],
    state="readonly",
    font=("Segoe UI", 14)
)
slctDrpdwn.pack(side="left", pady=7)
slctDrpdwn.bind("<<ComboboxSelected>>", on_dropdown_change)  # Fire callback on selection change

# Computer move display label
CompMve = tk.Label(root, textvariable=showComputerMove, font=("Segoe UI", 14))
CompMve.pack(anchor="w", pady=5)

# Result row: static "Result:" label + dynamic value label side by side
rsltFrame = tk.Frame(root)
rsltFrame.pack(anchor="w")

result_static = tk.Label(rsltFrame, text=" Result:", font=("Segoe UI", 14))
result_static.pack(side="left")

result_dynamic = tk.Label(rsltFrame, textvariable=showResult, font=("Segoe UI", 14))
result_dynamic.pack(side="left")

def on_button_click():
    """Handle Confirm button click: run game logic and display outcome."""
    playerMove = choicePlayerMove.get()                          # Read current dropdown selection
    computerMove = random.choice(['Rock', 'Paper', 'Scissors']) # Random computer move
    showComputerMove.set(' Computer Move: ' + computerMove)

    # Determine result
    if computerMove == playerMove:
        result = 'Draw'
        result_dynamic.config(foreground="#505050")   # Grey for draw
    elif playerMove == 'Rock' and computerMove == 'Scissors':
        result = 'Win'
        result_dynamic.config(foreground='green')
    elif playerMove == 'Rock' and computerMove == 'Paper':
        result = 'Loss'
        result_dynamic.config(foreground='red')
    elif playerMove == 'Scissors' and computerMove == 'Rock':
        result = 'Loss'
        result_dynamic.config(foreground='red')
    elif playerMove == 'Scissors' and computerMove == 'Paper':
        result = 'Win'
        result_dynamic.config(foreground='green')
    elif playerMove == 'Paper' and computerMove == 'Rock':
        result = 'Win'
        result_dynamic.config(foreground='green')
    elif playerMove == 'Paper' and computerMove == 'Scissors':
        result = 'Loss'
        result_dynamic.config(foreground='red')

    showResult.set(result)

# Confirm button
# Disabled by default; enabled only after a move is selected via on_dropdown_change
button = tk.Button(
    root,
    text="Confirm",
    command=on_button_click,
    font=("Segoe UI", 14),
    bg="#8B3030",          # Dark red when disabled
    activebackground="#007600",
    fg="#000000",
    state="disabled"
)
button.pack(side="bottom", fill="x", padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()