N = 4  # Change N for different board sizes
board = [[0 for _ in range(N)] for _ in range(N)]  # Initialize the board

def print_board():
    """Prints the chessboard with queens represented as 'Q' and empty spaces as '.'."""
    for i in range(N):
        for j in range(N):
            print("Q " if board[i][j] else ". ", end="")
        print()

def is_safe(row, col):
    """Checks if placing a queen at (row, col) is safe."""
    # Check column
    for i in range(row):
        if board[i][col]: 
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]: 
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]: 
            return False

    return True

def solve(row):
    """Solves the n-Queens problem using backtracking."""
    if row >= N: 
        return True  # All queens are placed

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1  # Place queen

            if solve(row + 1):  # Move to the next row
                return True

            board[row][col] = 0  # Backtrack

    return False  # No solution in this configuration

# Main execution
if __name__ == '__main__':
    board[0][1] = 1  # Place the first queen at (0, 1)

    if solve(1):  # Start solving from the second row
        print(f"Solution for the {N}-Queens problem:")
        print_board()
    else:
        print("No solution exists.")
