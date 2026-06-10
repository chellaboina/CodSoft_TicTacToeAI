board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_winner(player):
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True

    return False

while True:

    print_board()

    move = int(input("Enter position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = "X"

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if " " not in board:
        print_board()
        print("Draw!")
        break

    ai_move = board.index(" ")
    board[ai_move] = "O"

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break
