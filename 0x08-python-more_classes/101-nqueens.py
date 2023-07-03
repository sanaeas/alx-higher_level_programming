#!/usr/bin/python3
"""
Solve The N queens puzzle using Backtracking
"""
from sys import argv, exit


def nqueens(n):
    """a program that solves the N queens problem"""

    """Create an empty board"""
    board = [[i, None] for i in range(n)]

    def exists(x, y):
        """Check if a queen already exists in the same column (y)"""
        i = 0
        while i < x:
            if board[i][1] == y:
                return True
            i += 1
        return False

    def clear(x):
        """Clear the answers"""
        for i in range(x, n):
            board[i][1] = None

    def reject(x, y):
        """Reject the solution"""
        if exists(x, y):
            return False
        for i in range(x):
            if abs(board[i][1] - y) == abs(i - x):
                return False
        return True

    def solve_nqueens(x):
        """Recursive backtracking function"""
        for y in range(n):
            clear(x)
            if reject(x, y):
                board[x][1] = y
                if x == n - 1:
                    print(board)
                else:
                    solve_nqueens(x + 1)

    solve_nqueens(0)  # Start the recursive process at x = 0


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(argv[1]))
