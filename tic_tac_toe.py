"""
CSE210-01 Tic Tac Toe
Author: Heidi Munson
"""
#sqares in game board
board = ["1","2","3",
         "4","5","6",
        "7","8","9",]

def game():

    
    change_player = 0
    #loop through game until there is a winner
    while not check_winner(board) and change_player < 9:

        print_board()

        change_player = change_player + 1
        if change_player % 2 == 0:
            player = 'O'
        else:
            player = 'X'

       
        square = 0
        while square > 9 or square < 1:
            square = int(input(f"{player}\'s turn to choose a square (1-9): "))
            if square > 9 or square < 1:
                print('Please enter a valid number')

        board[square - 1] = player


    print_board()
    if change_player < 9:
        print(f"{player} is the winner!")
    else:
        print("Tie game")

#disply board
def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-+-+-')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-+-+-')
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()


#check board for winner
def check_winner(board):
    #check for winner by row, column, or diaganol
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

if __name__ == '__main__':
    game()

