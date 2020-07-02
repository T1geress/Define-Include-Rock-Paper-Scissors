import random
import tkinter as tk

result = "(no games played)"
#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output, result

    # 1. Create random integer 1-3 to use as computer's play
    computerchoice = random.randint(1, 3)

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if computerchoice == 1:
        computerchoice = "rock"
    if computerchoice == 2:
        computerchoice = "paper"
    if computerchoice == 3:
        computerchoice = "scissors"

    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object
    if call == computerchoice:
        result = "tied"
    if call == "scissors" and computerchoice == "paper":
        result = "won"
    if call == "rock" and computerchoice == "scissors":
        result = "won"
    if call == "paper" and computerchoice == "rock":
        result = "won"
    if call == "scissors" and computerchoice == "rock":
        result = "lost"
    if call == "rock" and computerchoice == "paper":
        result = "lost"
    if call == "paper" and computerchoice == "scissors":
        result = "lost"

    # If the user wins, increase win by 1
    if result == "won":
        win = win+1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    resultlabel.config(text = 'The computer chose ' + computerchoice + ' and you ' + result)
    winum.config(text = 'You have won ' + str(win) + ' times!')


# Use these functions as "command" for each button
def pass_s(event):
    get_winner("scissors")
def pass_r(event):
    get_winner("rock")
def pass_p(event):
    get_winner("paper")

window = tk.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE
# 1. Create 3 buttons for each option (rock, paper, scissors)
rock = tk.Button(
    window,
    text = 'Rock',
    width = 5,
    height = 2,
)
paper = tk.Button(
    window,
    text = 'Paper',
    width = 5,
    height = 2,
)
scissors = tk.Button(
    window,
    text = 'Scissors',
    width = 5,
    height = 2,
)
# 2. Create 2 labels for the result and the number of wins
resultlabel = tk.Label(window, text = 'No games played yet, push a button to start')
winum = tk.Label(window, text = 'You have won ' + str(win) + ' times.')
# 3. Arrange the buttons and labels using grid
rock.bind('<Button-1>', pass_r)
paper.bind('<Button-1>', pass_p)
scissors.bind('<Button-1>', pass_s)
resultlabel.grid(sticky = 'nw')
winum.grid(sticky = 'nw')
rock.grid(sticky = 'sw')
paper.grid(sticky = 'sw')
scissors.grid(sticky = 'sw')


window.mainloop()
