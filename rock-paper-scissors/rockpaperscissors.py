import random
import tkinter as tk

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    randint = randint(1, 3)

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if randint == 1:
        computerchoice = "rock"
    if randint == 2:
        computerchoice = "paper"
    if randint == 3:
        computerchoice = "scissors"

    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object


    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tk.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE
# 1. Create 3 buttons for each option (rock, paper, scissors)
rock = tk.Button(
    text = 'Rock',
    width = 5,
    height = 2
)
paper = tk.Button(
    text = 'Paper',
    width = 5,
    height = 2
)
scissors = tk.Button(
    text = 'Scissors',
    width = 5,
    height = 2
)
# 2. Create 2 labels for the result and the number of wins

winum = ('You have won ' + str(win) + ' times.')
# 3. Arrange the buttons and labels using grid
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
