import random

# Constants
EMPTY = ' '
WALL = '|'
PACMAN = 'C'
GHOST = 'G'
DOT = '.'

# Define the game board
board = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, DOT, DOT, DOT, DOT, DOT, DOT, DOT, DOT, WALL],
    [WALL, DOT, WALL, WALL, WALL, WALL, WALL, WALL, DOT, WALL],
    [WALL, DOT, DOT, DOT, DOT, DOT, DOT, DOT, DOT, WALL],
    [WALL, DOT, WALL, DOT, WALL, DOT, WALL, DOT, WALL, WALL],
    [WALL, DOT, WALL, DOT, WALL, DOT, WALL, DOT, WALL, WALL],
    [WALL, DOT, DOT, DOT, DOT, DOT, DOT, DOT, DOT, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
]

# Function to print the game board
def print_board():
    for row in board:
        print(''.join(row))

# Function to place Pac-Man and Ghost randomly on the board
def place_characters():
    while True:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board[0]) - 1)
        if board[x][y] == DOT:
            board[x][y] = PACMAN
            break

    while True:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board[0]) - 1)
        if board[x][y] == DOT:
            board[x][y] = GHOST
            break

# Function to move Pac-Man
def move_pacman(direction):
    global pacman_x, pacman_y
    if direction == 'up':
        if board[pacman_x - 1][pacman_y] != WALL:
            board[pacman_x][pacman_y] = EMPTY
            pacman_x -= 1
    elif direction == 'down':
        if board[pacman_x + 1][pacman_y] != WALL:
            board[pacman_x][pacman_y] = EMPTY
            pacman_x += 1
    elif direction == 'left':
        if board[pacman_x][pacman_y - 1] != WALL:
            board[pacman_x][pacman_y] = EMPTY
            pacman_y -= 1
    elif direction == 'right':
        if board[pacman_x][pacman_y + 1] != WALL:
            board[pacman_x][pacman_y] = EMPTY
            pacman_y += 1

# Main game loop
def main():
    global pacman_x, pacman_y
    place_characters()
    pacman_x, pacman_y = 1, 1

    while True:
        print_board()
        direction = input("Enter direction (up/down/left/right): ").lower()
        move_pacman(direction)

        # Check for game over condition
        if board[pacman_x][pacman_y] == GHOST:
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
