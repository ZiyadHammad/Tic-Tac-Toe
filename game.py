import random

def initialize_board():
    return [' ' for _ in range(9)]

def display_board(board):
    rows = [
        f" {board[0]} | {board[1]} | {board[2]} ",
        f" {board[3]} | {board[4]} | {board[5]} ",
        f" {board[6]} | {board[7]} | {board[8]} "
    ]
    
    print("-" * 13)
    
    for row in rows:
        print(f"|{row}|")
        print("-" * 13)

def get_player_input(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("This cell is already occupied. Please choose another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def make_move(board, move, player):
    board[move] = player

def choose_player():
    while True:
        player = input("Choose your symbol: 'X' or 'O': ").upper()
        if player == 'X' or player == 'O':
            return player
        else:
            print("Invalid choice: Please select either 'X' or 'O'." )

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def check_tie(board):
    return ' ' not in board

def computer_move(board, computer_player):
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)

# Main Game Loop
def main():
    board = initialize_board()
    player = choose_player()
    computer_player = 'O' if player == 'X' else 'X'
    
    current_player = player

    while True:
        display_board(board)
        
        if current_player == player:
            move = get_player_input(board, player)
        else:
            move = computer_move(board, computer_player)
            print(f"Computer ({computer_player}) chooses move {move + 1}")
        
        make_move(board, move, current_player)
        
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = computer_player if current_player == player else player

# Start the game
main()