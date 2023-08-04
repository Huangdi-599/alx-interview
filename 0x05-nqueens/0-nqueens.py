#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, row):
    n = len(board)
    if row == n:
        for row in board:
            print([[r, c] for r, c in enumerate(row) if c == 1])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_queens(board, row + 1)
            board[row][col] = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an NxN chessboard
    chessboard = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_queens(chessboard, 0)

    sys.exit(0)
