from sudoku import print_board
a = [[0 for i in range(9)] for j in range(9)]
for position in positions:
    a[position[0]][position[1]] = "+"
print_board(a )