def print_board(board):
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("-----------")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]

    return None

def play_tic_tac_toe():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'

    while True:
        print_board(board)

        move = int(input("Player {}, enter your move (1-9): ".format(player)))
        move -= 1

        if board[move] == ' ':
            board[move] = player
        else:
            print("Invalid move. Please try again.")
            continue

        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Player {} wins!".format(player))
            break
        elif ' ' not in board:
            print_board(board)
            print("Game over. It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
