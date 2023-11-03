#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """

import sys

class NQueen:
    """ Class for solving N Queen Problem """
    
    def __init__(self, n):
        """ Initialize N Queen Problem with n queens """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.solutions = []

    def can_place_queen(self, k, i):
        """ Check if a queen can be placed at column i for the kth row """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def solve_n_queens(self, k):
        """ Solve the N Queen problem recursively """
        for i in range(1, self.n + 1):
            if self.can_place_queen(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = [[row - 1, col - 1] for row, col in enumerate(self.x[1:], start=1)]
                    self.solutions.append(solution)
                else:
                    self.solve_n_queens(k + 1)

    def find_solutions(self):
        """ Find all solutions to the N Queen problem """
        self.solve_n_queens(1)
        return self.solutions

if __name__ == "__main":
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

    queen = NQueen(N)
    solutions = queen.find_solutions()

    for solution in solutions:
        print(solution)
