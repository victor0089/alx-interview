#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    """
    Recursively solve the N queens problem for a given row.
    """
    # Base case: If all queens are placed, print the solution
    if row == len(board):
        print_solution(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen and recursively solve for the next row
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            # Backtrack: Remove the queen if the solution is not valid
            board[row][col] = 0

def print_solution(board):
    """
    Print the solution board.
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def main():
    """
    Main function to parse command line arguments and solve the N queens problem.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse and validate the input N
    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number and at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N queens problem
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()
