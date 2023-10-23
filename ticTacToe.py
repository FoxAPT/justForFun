# By Wes Miller
# COP2002-0T2
# Sept 6, 2023
# Tic Tac Toe Game
# Allow two players to play the game Tic Tac Toe

print("WELCOME TO A GAME OF TIC TAC TOE!")

# Function to print the game board
def print_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to check if a move is valid
def is_valid_move(row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

# Function to check if a player has won
def check_win(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Input player names.
player_one = input("\n\nPlayer One, what is your name? ")
player_two = input("\nPlayer Two, what is your name? ")

# Main game loop
player_turn = 'X'
while True:
    print("\nCurrent board:")
    print_board()
    print(f"\n{player_one} (X) vs. {player_two} (O)")

    # Get the player's move
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if is_valid_move(row, col):
                break
            else:
                print("\nInvalid move. Try again.")
        except ValueError:
            print("\nInvalid input. Please enter numbers.")

    # Update the board with the player's move
    board[row][col] = player_turn

    # Check if the player has won
    if check_win(player_turn):
        print_board()
        print(f"\n{player_turn} ({player_one if player_turn == 'X' else player_two}) wins!")
        break

    # Check for a draw (all cells filled)
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        print_board()
        print("\nIt's a draw!")
        break

    # Switch to the other player's turn
    player_turn = 'O' if player_turn == 'X' else 'X'

input("Do you want to play again? (Yes or No): ")
play_again = input().lower()

if play_again == "Yes":
    print("Let's play")
