from collections import namedtuple

# board = [
#   ['_', '_', '_'],
#   ['_', '_', '_'],
#   ['_', '_', '_'],
# ]

board = [['_']*3 for i in range(3)]

moves = 0

def place(symbol: str, row: int, col: int) -> None:
  global moves
  if board[row][col] != '_':
    if moves >= 9:
      print('ITS A DRAW')
      return
    print("PLACE ALREADY TAKEN. TRY AGAIN")
    return
  board[row][col] = symbol
  moves += 1
  if(hasWon(symbol)): 
    print(f'{symbol} has won!')
  else: 
    print('move has been made!')

  


def hasWon(symbol: str):
  for i in range(3):
    if hasWon_(symbol, 0, i) or hasWon_(symbol, i, 0):
      return True
  return False


def hasWon_(symbol: str, row, col):
  Point = namedtuple('Point', ['row', 'col', 'streak'])
  queue = [Point(row, col, 0 if board[row][col] != symbol else 1)]
  visited = set([(row, col)])
  while(len(queue)):
    current = queue.pop(0)

    if current.streak == 3:
      return True
    
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1)]
    for deltaRow, deltaCol in deltas:
      currentSymbol = board[current.row][current.col]
      newRow, newCol = [current.row + deltaRow, current.col + deltaCol]

      if not (0 <= newRow and newRow < len(board)):
        continue

      if not (0 <= newCol and newCol < len(board[0])):
        continue

      if (newRow, newCol) in visited:
        continue
      
      if board[newRow][newCol] == symbol:
        # print(f'adding {(newRow, newCol)}')
        if currentSymbol == symbol:
          queue.append(Point(newRow, newCol, current.streak + 1))
        else: 
          queue.append(Point(newRow, newCol, 0))
        visited.add((newRow, newCol))
        # print(queue)
  return False

      
      




place('X', 0, 0)
place('X', 1, 0)
place('X', 2, 0)
# print(board)
# print(hasWon('X'))
# print(hasWon_('X', 0, 0))
# print(moves)
# print(board)