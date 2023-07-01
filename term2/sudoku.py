import tkinter
import numpy as np
from tkinter import filedialog
import json
import copy 

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


def find_first_empty_position(board):
    for i in range(9):
        for j in range(9):
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

    # check column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check cube
    cube_x = position[1] // 3
    cube_y = position[0] // 3

    for i in range(cube_y * 3, cube_y * 3 + 3):
        for j in range(cube_x * 3, cube_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def validate_board(board):
    # returns true if board is solveable
    clone = copy.deepcopy(board)
    return solve_board(clone)

def solve_board(board):
    empty_position = find_first_empty_position(board)

    # base case
    if not empty_position:
        return True
    else:
        row, col = empty_position

    for i in range(1, 10):
        if is_Valid(board, (row, col), i):
            board[row][col] = i

            # backtrack and try again
            if solve_board(board):
                return True
            board[row][col] = 0

    return False


def gen_random_board(number_of_empty_cells=30):
    board = [np.zeros(9) for i in range(9)]
    board[np.random.randint(9)][np.random.randint(9)] = np.random.randint(1, 10)
    solve_board(board)

    cells_to_empty = []

    def gen_random_cell():
        return [np.random.randint(9), np.random.randint(9)]

    # add `number_of_empty_cells` unique cells to cells_to_empty
    for i in range(number_of_empty_cells):
        while True:
            t = gen_random_cell()
            if not t in cells_to_empty:
                cells_to_empty.append(t)
                break
    for cell in cells_to_empty:
        board[cell[0]][cell[1]] = 0

    return board


class GUI:
    @property
    def labels_data(self):
        t = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                t[i].append(
                    int(float(self.entry_controlled_variables[i * 9 + j].get() or 0 ))
                )
        return t

    @labels_data.setter
    def labels_data(self, new_value):
        for row in range(9):
            for col in range(9):
                self.entry_controlled_variables[row * 9 + col].set(
                    str(new_value[row][col])
                )

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("500x500")
        self.entry_controlled_variables = [
            tkinter.StringVar(self.window, 0) for i in range(81)
        ]
        # creating label components
        self.labels = []
        for i in range(81):
            l = tkinter.Entry(
                self.window, textvariable=self.entry_controlled_variables[i]
            )
            cor = self.index_to_cordinates(i)

            l.grid(row=cor[0], column=cor[1])
            self.labels.append(l)

        # create difficulty radio buttons
        self.radio_buttons_variable = tkinter.IntVar(self.window, 30)

        t = tkinter.Radiobutton(
            self.window, text="easy", value=30, variable=self.radio_buttons_variable
        )
        t.grid(row=10, column=1)
        t = tkinter.Radiobutton(
            self.window, text="medium", value=40, variable=self.radio_buttons_variable
        )
        t.grid(row=10, column=2)
        t = tkinter.Radiobutton(
            self.window, text="hard", value=50, variable=self.radio_buttons_variable
        )
        t.grid(row=10, column=3)

        # create control menu
        t = tkinter.Button(self.window, text="create", command=self.create)
        t.grid(row=11, column=1)
        t = tkinter.Button(self.window, text="load", command=self.load)
        t.grid(row=11, column=2)
        t = tkinter.Button(self.window, text="solve", command=self.solve)
        t.grid(row=11, column=3)
        t = tkinter.Button(self.window, text="check", command=self.check)
        t.grid(row=11, column=4)

        self.window.mainloop()

    def load(self):
        filename = filedialog.askopenfilename(title="select a file")
        new_labels_data = []
        for line in open(filename, "r"):
            new_labels_data.append([int(cell) for cell in line.split(",")])
        self.labels_data = new_labels_data

    def create(self):
        self.labels_data = gen_random_board(self.radio_buttons_variable.get())

    def solve(self):
        clone = copy.deepcopy(self.labels_data)
        solve_board(clone)
        self.labels_data = clone 

    def check(self):
        if validate_board(self.labels_data) == True:
            tkinter.messagebox.showinfo(
                title="board validation result", message="board is valid"
            )
        else:
            tkinter.messagebox.showerror(
                title="board validation result", message="board is invalid"
            )

    def index_to_cordinates(self, index):
        return [index // 9, index % 9]


GUI()
