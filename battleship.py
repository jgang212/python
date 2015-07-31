
"""
Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!
"""

from random import randint

# print formatted board
def print_board(board):
    for row in board:
        print " ".join(row)

# create blank board
board = []
board_size = 5

for x in range(board_size):
    board.append(["O"] * board_size)

# game starts
print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)
while ship1_row == ship2_row and ship1_col == ship2_col:
    ship2_row = random_row(board)
    ship2_col = random_col(board)

for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship1_row and guess_col == ship1_row:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > board_size - 1) or (guess_col < 0 or guess_col > board_size - 1):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        if turn == 3:
            print "Game Over"
        print_board(board)