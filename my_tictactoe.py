'''
Game of Tic-Tac-Toe.
Author: Isaac Asiedu
'''

def main():
    player = next_player("")
    board = make_a_board()
     
    while not (make_the_winner(board) or is_a_draw(board)):
        board_display(board)
        make_move(player, board)
        player = next_player(player)
    board_display(board)
    print_scoreboard(board, player)
    

def make_a_board():
    board = []
    for box in range(9):
        board.append(box + 1)
    return board


def board_display(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")


def make_the_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def is_a_draw(board):   
    for box in range(9):
        if board[box] != "X" and board[box] != "O":
            return False
    return True


def make_move(player, board):
    box = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[box - 1] = player


def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"


def print_scoreboard(board, player):
    score_board = 1
    
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    for box in range(1):
        if board[box] == "X" :
            player = "X"
            print("\t   ", player, "\t    ", score_board)
            
        else:
            board[box] == "O"
            player = "O"
            print("\t   ", player, "\t    ", score_board)
            
    print("\t--------------------------------")
    print(f"\t          {player} is the winner\n")

    print("\t  Good game. Thanks for playing!")
    print("\t--------------------------------\n")
    

if __name__ == "__main__":
    main()
