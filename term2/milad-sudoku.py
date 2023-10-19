import tkinter as tk
import copy
import random
from tkinter import filedialog

class Sudoko_Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("sudoko_Game")
        self.root.geometry("550x550")
        self.root.resizable(width=False, height=False)
        self.controlled_variables = [
            ([tk.StringVar(self.root, "0") for col in range(9)]) for row in range(9)
        ]
        for row in range(9):
            for column in range(9):
                tk.Entry(
                    self.root,
                    width=1,
                    textvariable=self.controlled_variables[row][column],
                ).grid(row=row, column=column)

        self.radio_button_state = tk.IntVar(self.root,30)
        tk.Radiobutton(self.root , value=30 , text="easy" , variable=self.radio_button_state).grid(row = 11,column= 1)
        tk.Radiobutton(self.root , value=40 , text="medium" , variable=self.radio_button_state).grid(row = 11,column= 2)
        tk.Radiobutton(self.root , value=50 , text="hard" , variable=self.radio_button_state).grid(row = 11,column= 3)

        tk.Button(self.root, text="load", command=self.load_button_onclick).grid(row = 10,column=1)
        tk.Button(self.root, text="check", command=self.check_button_onclick).grid(row = 10,column=2)
        tk.Button(self.root, text="solve ", command=self.solve_button_onclick).grid(row = 10,column=3)
        tk.Button(self.root, text="create ", command=self.create_button_onclick).grid(row = 10,column=4)

        tk.mainloop()

    @property
    def board(self):
        return [
            [int(float(self.controlled_variables[row][col].get())) for col in range(9)]
            for row in range(9)
        ]

    @board.setter
    def board(self, new_value):
        for i in range(9):
            for j in range(9):
                self.controlled_variables[i][j].set(new_value[i][j])


    

    def solve_button_onclick(self):
        clone = copy.deepcopy(self.board)
        self.solving_sudoku(clone, 0, 0)
        # todo inform the user if that sudoku is not solvable
        self.board = clone

    def load_button_onclick(self):
        filename = filedialog.askopenfilename()
        t = []
        for line in open(filename, "r"):
            t.append([int(i) for i in line.split(",")])
        self.board = t

    def check_button_onclick(self):
        t = copy.deepcopy(self.board)
        if not self.is_valid(t):
            tk.messagebox.showinfo(title ='check status ' , message = 'this board is not solvable')
        else:
            tk.messagebox.showinfo(
                title="check status", message="this board is solvable"
            )

    def create_button_onclick(self):
        t = [[0 for i in range(9)] for j in range(9)]
        rand_numbers = [random.randint(0,8) for i in range(2)]
        t[rand_numbers[0]][rand_numbers[1]] = random.randint(1,9)
        self.solving_sudoku(t, 0, 0)
        all_possible_cells = []
        for i in range(9):
            for j in range(9):
                all_possible_cells.append([i,j])
        
        cells_to_empty = random.sample(all_possible_cells , int(float(self.radio_button_state.get())))
        
        for cell in cells_to_empty:
            if(cells_to_empty.count(cell) > 1) :
                raise RuntimeError('there is duplication in cells_to_empty. just run it again')
        
        for cell in cells_to_empty :
            t[cell[0]][cell[1]] = 0
        self.board = t
    def is_valid(self , board):
        # check row
        for row in board:
            for number in range(1, 10):
                if row.count(number) > 1:
                    return False

        # check column
        for col_index in range(9):
            col = []
            for row in board:
                col.append(row[col_index])
            for number in range(1,10):
                if col.count(number) > 1:
                    return False

        # check cube
        positions = [
            [0, 0],
            [0, 3],
            [0, 6],
            [3, 0],
            [3, 3],
            [3, 6],
            [6, 0],
            [6, 3],
            [6, 6],
        ]

        for number in range(1, 10):
            for position in positions:
                cube_x = position[1] // 3
                cube_y = position[0] // 3
                cube_cells = []
                for i in range(cube_y * 3, cube_y * 3 + 3):
                    for j in range(cube_x * 3, cube_x * 3 + 3):
                        cube_cells.append(board[i][j])
                if cube_cells.count(number) > 1:
                    return False

        return True

    def can_be_put(self , grid, position, number):
        # in that row and col and cube that position is located in there is not any
        # other cell with number= that number we want to put in this position
        t = copy.deepcopy(grid)
        t[position[0]][position[1]] = number
        return self.is_valid(t)

    def solving_sudoku(self, grid, row, column):
        if column == 9:
            if row == 8:
                return True
            else:
                row += 1
                column = 0
        if grid[row][column] > 0:
            return self.solving_sudoku(grid, row, column + 1)

        for number in range(1, 10):
            if self.can_be_put(grid,[ row, column], number):
                grid[row][column] = number

                if self.solving_sudoku(grid, row, column + 1):
                    return True
            grid[row][column] = 0
        return False

t = Sudoko_Gui()
