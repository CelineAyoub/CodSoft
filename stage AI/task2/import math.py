import math

# Constants to represent different players
HUMAN = -1
AI = 1
EMPTY = 0

# Function to print the board
def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == HUMAN:
                print(" X ", end="|")
            elif cell == AI:
                print(" O ", end="|")
            else:
                print("   ", end="|")
        print("\n-------------")

# Function to check if the game is over
def game_over(board):
    return check_winner(board) or len(empty_cells(board)) == 0

# Function to check if there's a winner
def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == HUMAN for cell in row):
            return HUMAN
        elif all(cell == AI for cell in row):
            return AI

    # Check columns
    for col in range(3):
        if all(board[row][col] == HUMAN for row in range(3)):
            return HUMAN
        elif all(board[row][col] == AI for row in range(3)):
            return AI

    # Check diagonals
    if all(board[i][i] == HUMAN for i in range(3)):
        return HUMAN
    elif all(board[i][2-i] == AI for i in range(3)):
        return AI

    return None

# Function to return empty cells
def empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_winner(board) == AI:
        return 1
    elif check_winner(board) == HUMAN:
        return -1
    else:
        return 0

# Minimax function with alpha-beta pruning
def minimax(board, depth, alpha, beta, player):
    if player == AI:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, -1, score]

    for cell in empty_cells(board):
        row, col = cell
        board[row][col] = player
        score = minimax(board, depth - 1, alpha, beta, -player)
        board[row][col] = EMPTY
        score[0], score[1] = row, col

        if player == AI:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, best[2])

        if alpha >= beta:
            break

    return best

# Function for the AI to make a move
def ai_turn(board):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        return 0, 0

    if depth == 8:
        if board[1][1] == EMPTY:
            return 1, 1
        else:
            return 0, 0

    if depth <= 6:
        move = minimax(board, depth, -math.inf, math.inf, AI)
        return move[0], move[1]

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        row, col = None, None
        while (row, col) not in empty_cells(board):
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

        board[row][col] = HUMAN
        print_board(board)

        if game_over(board):
            break

        ai_row, ai_col = ai_turn(board)
        board[ai_row][ai_col] = AI
        print("AI's move:")
        print_board(board)

    winner = check_winner(board)
    if winner == AI:
        print("AI wins!")
    elif winner == HUMAN:
        print("Human wins!")
    else:
        print("It's a tie!")

play_game()
