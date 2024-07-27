import math

# Define the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print('| '.join(row))
        print('-' * 5)

# Function to check if the game has been won
def is_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

# Function to check if the board is full
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Utility function for the terminal state
def utility(player):
    if is_winner(player):
        return 10 if player == 'X' else -10
    return 0

# Minimax with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta, player, opponent):
    # Terminal state or maximum depth reached
    score = utility(opponent)
    if score != 0 or is_board_full() or depth == 0:
        return score

    if is_maximizing:
        best_value = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    value = minimax(depth - 1, False, alpha, beta, player, opponent)
                    board[i][j] = ' '  # Undo the move
                    best_value = max(best_value, value)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best_value
    else:
        best_value = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = opponent
                    value = minimax(depth - 1, True, alpha, beta, player, opponent)
                    board[i][j] = ' '  # Undo the move
                    best_value = min(best_value, value)
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best_value

# Function to get the best move for the AI
def get_best_move(player, opponent):
    best_value = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                value = minimax(2, False, -math.inf, math.inf, player, opponent)
                board[i][j] = ' '  # Undo the move
                if value > best_value:
                    best_value = value
                    move = (i, j)
    return move

# Main game loop
def play_game():
    current_player = 'X'  # Human player
    ai_player = 'O'       # AI player

    while True:
        print_board()

        # Human player's turn
        if current_player == 'X':
            while True:
                try:
                    x, y = map(int, input("Enter your move (row col): ").split())
                    if board[x][y] == ' ':
                        board[x][y] = current_player
                        break
                    else:
                        print("This position is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter two numbers between 0 and 2 separated by a space.")
        # AI player's turn
        else:
            print("AI is making a move...")
            x, y = get_best_move(ai_player, current_player)
            board[x][y] = current_player

        # Check for a winner or a draw
        if is_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()