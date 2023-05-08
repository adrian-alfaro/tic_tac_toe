# Importing libraries
from random import randrange

# Creating board----------------------------------------------------
board_vals = [[x for x in range(1,4)],[x for x in range(4,7)],[x for x in range(7,10)]]
print(board_vals)

# First move by the computer is X in the middle
board_vals[1][1]= 'X'
print(board_vals)

# Board backbone
hori_lines = ('+'+'-'*7)*3+'+\n'
vert_lines = ('|'+' '*7)*3+'|\n'

#Creating loop funtion
def display_board():
    for row in board_vals:
        val_lines = '|'+' '*3+str(row[0])+' '*3+\
                    '|'+' '*3+str(row[1])+' '*3+\
                    '|'+' '*3+str(row[2])+' '*3+'|\n'
        print(hori_lines+vert_lines+val_lines+vert_lines, end='')
    
    print(hori_lines)

# funtion that resets the board------------------------------------------
def reset():
    global board_vals
    board_vals = [[x for x in range(1,4)],[x for x in range(4,7)],[x for x in range(7,10)]]
    board_vals[1][1]= 'X'

# Dictionary maps the numbers to their location in the nested list--------
coor = {1:[0,0],
        2:[0,1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2]
       }

# Checker funtion----------------------------------------------------------

#found = False

def checker(move=9):
    col = 0

# checks if the "user move" is available and if it is a number, returns the value
    for row in board_vals:
        for col in row:
            if col == move and type(move) is int:
                global next_move
                next_move = move
                return move
                break
    return False   

# Updates the board based on next move--------------------------------------
def update_user():
    board_vals[coor[next_move][0]][coor[next_move][1]] = 'O'
    
def update_computer():
    board_vals[coor[next_move][0]][coor[next_move][1]] = 'X'

# Loop that asks the user to enter the next move, and then checks if it is valid

def check_user():
    invalid = True

    while invalid:
        if checker(int(input('Please enter your next move: '))):
            update_user()
            display_board()
            invalid = False
        else:
            print('\nplease try again, your number is not on the board\n')
            display_board()

def check_computer():
    invalid = True

    while invalid:
        if checker(randrange(1,10)):
            update_computer()
            print('The computer choose: ',next_move)
            display_board()
            invalid = False


# This code checks is there is the same value in a row, column, or diagonal, to declare a winner or continue

def winner_check():
    
    #Checks rows -------------------------------------------------
    if board_vals[0][0] == board_vals[0][1] == board_vals[0][2]:
        return board_vals[0][0]
    
    elif board_vals[1][0] == board_vals[1][1] == board_vals[1][2]:
        return board_vals[1][0]
    
    elif board_vals[2][0] == board_vals[2][1] == board_vals[2][2]:
        return board_vals[2][0]
    #Checks columns ----------------------------------------------
    elif board_vals[0][0] == board_vals[1][0] == board_vals[2][0]:
        return board_vals[0][0]
    
    elif board_vals[0][1] == board_vals[1][1] == board_vals[2][1]:
        return board_vals[0][1]
    
    elif board_vals[0][2] == board_vals[1][2] == board_vals[2][2]:
        return board_vals[0][2]
    #Checks diagonals --------------------------------------------
    elif board_vals[0][0] == board_vals[1][1] == board_vals[2][2]:
        return board_vals[1][1]
    
    elif board_vals[2][0] == board_vals[1][1] == board_vals[0][2]:
        return board_vals[1][1]
    #No winner yet -----------------------------------------------
    else:
        print('no winner yet')
        return False
    
# here is where the game starts:-----------------------------------------
reset()
print('-----------------------------------------------------------------------------------------------\n'
      '\n\nWelcome to Tic, Tac, Toe\n\n')
display_board()
print('As you can see the computer went first, How rude!\n\n\n'
      'Now its your turn, you can select a square by typing one of the available numbers on the screen\n'
      'Rememeber, you are playing with the circles "O"\n\nGood luck!')

for i in range(4):
    check_user()
    check_computer()
    if winner_check():
        if winner_check() == 'O':
            print("Ganaste!")
        else:
            print("Perdiste, la computadora gana")
        break