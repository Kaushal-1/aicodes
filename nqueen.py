def is_safe(board, col, row):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]  # Create an empty chessboard
    solutions = []

    def backtrack(row):
        # If we've placed queens in all rows, we've found a solution
        if row == N:
            solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
            return

        for col in range(N):
            if is_safe(board, col, row):
                board[row][col] = 1  # Place the queen
                backtrack(row + 1)  # Recur to the next row
                board[row][col] = 0  # Backtrack (remove the queen)

    backtrack(0)  # Start with the first row
    return solutions

def print_solutions(solutions):
    """
    Print all solutions to the N-Queens problem.
    """
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

N = 4
solutions = solve_n_queens(N)
if solutions:
    print_solutions(solutions)
else:
    print("No solution found.")
