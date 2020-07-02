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
    text = 'Rock',
    width = 5,
    height = 2,
    relief = RAISED
)
paper = tk.Button(
    text = 'Paper',
    width = 5,
    height = 2,
    relief = RAISED
)
scissors = tk.Button(
    text = 'Scissors',
    width = 5,
    height = 2,
    relief = RAISED
)
# 2. Create 2 labels for the result and the number of wins
result = tk.Label('The computer chose ' + computerchoice + ' and you ' + result)
winum = tk.Label('You have won ' + str(win) + ' times.')
# 3. Arrange the buttons and labels using grid
rock.bind('<Button-1>', pass_r)
paper.bind('<Button-1>', pass_p)
scissors.bind('<Button-1>', pass_s)
result.grid(sticky = nw)
wins.grid(sticky = nw)
rock.grid(sticky = sw)
paper.grid(sticky = sw)
scissors.grid(sticky = sw)


window.mainloop()
