import numpy as np 
# code is forked from : https://github.com/kubicodes/Backtracking-Sudoku-Solver-with-Python.git
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def is_Valid(board, position, number):
    # in that row and col and cube that position is located in there is not any
    # other cell with number= that number we want to put in this position 
    
    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #check column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #check cube
    cube_x = position[1] // 3
    cube_y = position[0] // 3

    for i in range(cube_y * 3, cube_y * 3 + 3):
        for j in range(cube_x * 3, cube_x * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

def solve_board(board):
    empty_position = find_empty_position(board)

    #base case
    if not empty_position:
        return True
    else:
        row, col = empty_position

    for i in range(1, 10):
        if is_Valid(board, (row, col), i):
            board[row][col] = i

            #backtrack and try again
            if solve_board(board):
                return True
            board[row][col] = 0

    return False

def gen_random_board(number_of_empty_cells=30):
    board = [np.zeros(9) for i in range(9)]
    board[np.random.randint(9)][np.random.randint(9)] = np.random.randint(1,10)
    solve_board(board)

    cells_to_empty = []
    def gen_random_cell():
        return [np.random.randint(9),np.random.randint(9)]

    #add `number_of_empty_cells` unique cells to cells_to_empty 
    for i in range(number_of_empty_cells):
        while True :
            t = gen_random_cell()
            if not t in cells_to_empty:
                cells_to_empty.append(t)
                break
    for cell in cells_to_empty:
        
        board[cell[0]][cell[1]] = 0 
    

    return board
            