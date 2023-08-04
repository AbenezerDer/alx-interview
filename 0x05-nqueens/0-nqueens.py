import sys

def is_attacked(board, row, col):
  for i in range(row):
    if board[i][col] == 1:
      return True

  for i in range(row - 1, -1, -1):
    for j in range(col - 1, -1, -1):
      if board[i][j] == 1 and (row - i == col - j or row - i == j - col):
        return True

  for i in range(row + 1, len(board)):
    for j in range(col - 1, -1, -1):
      if board[i][j] == 1 and (i - row == col - j or i - row == j - col):
        return True

  return False

def nqueens(board, n, row):
  if row == n:
    print(*board)
    return

  for col in range(n):
    if not is_attacked(board, row, col):
      board[row][col] = 1
      nqueens(board, n, row + 1)
      board[row][col] = 0

def main():
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number")
    sys.exit(1)

  if n < 4:
    print("N must be at least 4")
    sys.exit(1)

  board = [[0 for _ in range(n)] for _ in range(n)]
  nqueens(board, n, 0)

if __name__ == "__main__":
  main()