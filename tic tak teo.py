# ye function se board banega.
def print_board(board):
  for i in range(3):
    print("| {} | {} | {} |".format(board[i][0], board[i][1], board[i][2]))

# ye function winners ko check karta h.
def check_winner(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != " ":
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] != " ":
      return board[0][i]
    if board[i][0] == board[1][1] == board[2][2] != " ":
      return board[i][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
      return board[0][2]
  return None

# ye turn ke liye h.
def get_player_move(player):
  while True:
    move = input("Player {} enter your move (1-9): ".format(player))
    try:
      move = int(move) - 1
      if 0 <= move <= 8:
        return move
    except ValueError:
      pass
    print("Invalid move. Please try again.")

# isse hum khelenge.
def play_game():
  board = [[" " for i in range(3)] for j in range(3)]
  player = 1
  while True:
    print_board(board)
    move = get_player_move(player)
    board[move // 3][move % 3] = "X" if player == 1 else "O"
    winner = check_winner(board)
    if winner is not None:
      print("Player {} wins!".format(winner))
      break
    player = 2 if player == 1 else 1

# function call.
play_game()