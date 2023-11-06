def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, solutions):
    n = len(board)
    if col >= n:
        solutions.append([[1 if cell == 1 else 0 for cell in row] for row in board])
        return
    
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, col + 1, solutions)
            board[row][col] = 0


def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, solutions)

    return solutions

n = int(input("Enter the value of n: "))

solutions = solve_nqueens(n)
print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(" ".join(str(cell) for cell in row))
    print()