
"""
Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!
"""

from random import randint
from inputs import positiveIntInput

# print formatted board
def print_board(board):
    for row in board:
        print " ".join(row)

# find random row and col for ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# create a board
def create_board(board_size):
    board = []
        
    for x in range(board_size):
        board.append(["O"] * board_size)
    return board

# get ship coordinates for board
def get_ship_coordinates(board, numShips):
    shipCoordinates = []
    
    for i in range(0,numShips):
        shipRow = random_row(board)
        shipCol = random_col(board)
        
        # to make sure that ships don't have identical coordinates
        if i > 0:
            while True:
                if [item for item in shipCoordinates if item[0] == shipRow and item[1] == shipCol]:
                    shipRow = random_row(board)
                    shipCol = random_col(board)
                else:
                    break
        shipCoordinates.append((shipRow, shipCol))
        
    return shipCoordinates
    
###############################################

# game starts
print "Let's play Battleship!"
numTurns = positiveIntInput("How many turns do you want? ")

# create blank board
while True:
    board_size = positiveIntInput("How big of a square board shall we play with? ")
    if board_size < 2:
        print "The board needs to be at least 2x2 to play!"
    else:
        break
board = create_board(board_size)
print_board(board)

# place ships randomly
while True:
    numShips = positiveIntInput("How many ships do I have on the board? ")
    if numShips == 0:
        print "There needs to be at least one ship to play!"
    elif numShips > board_size**2:
        print "There are too many ships for this board!"
    else:
        break
shipCoordinates = get_ship_coordinates(board, numShips)

shipsRemaining = numShips
for turn in range(numTurns):
    if shipsRemaining == 0:
        print "Congratulations! You sunk all of my battleships!"
        break
    
    print "-------------------------------"
    print "Turn", turn + 1    
    
    guess_row = positiveIntInput("Guess Row: ")
    guess_col = positiveIntInput("Guess Col: ")
    
    if (guess_row < 0 or guess_row > board_size - 1) or (guess_col < 0 or guess_col > board_size - 1):
        print "Oops, that's not even in the ocean."
    elif (board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "S"):
        print "You guessed that one already."
    elif [item for item in shipCoordinates if item[0] == guess_row and item[1] == guess_col]:
        print "You sunk a battleship!"
        shipsRemaining = shipsRemaining - 1
        board[guess_row][guess_col] = "S"
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    
    print "Ships remaining:", shipsRemaining    
    
    if turn == numTurns - 1:
        print "Game Over"
    print_board(board)