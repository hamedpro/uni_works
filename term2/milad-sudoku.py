import tkinter as tk
import copy
import random


class Sudoko_Gui:
    def __init__(self):
        self.grid = [[0] * 9] * 9
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
                    width=4,
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
            [self.controlled_variables[row][col].get() for col in range(9)]
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
        filename = tk.filedialog.askopenfilename()
        t = []
        for line in open(filename, "r"):
            t.append([int(i) for i in line.split(",")])
        self.board = t

    def check_button_onclick(self):
        t = copy.deepcopy(self.board)
        if self.solving_sudoku(t, 0, 0):
            tk.messagebox.showinfo(
                title="validation result", message="this board is valid"
            )
        else:
            tk.messagebox.showerror(
                title="validation result", message="this board is invalid"
            )

    def create_button_onclick(self):
        t = [[0 for i in range(9)] for j in range(9)]
        rand_numbers = [random.randint(0,9) for i in range(3)]
        print(rand_numbers)
        t[rand_numbers[0]][rand_numbers[1]] = rand_numbers[2]
        self.solving_sudoku(t, 0, 0)
        cells_to_empty = [[random.randint(1, 10) for i in range(2)] for i in range(self.radio_button_state.get())]
        #todo check if there is any duplication in cells_to_empty 
        for cell in cells_to_empty :
            t[cell[0]][cell[1]] = 0
        self.board = t

    def is_valid(self, grid, row, column, number):
        if number in grid[row]:
            return False
        for x in range(9):
            if grid[x][column] == number:
                return False
        row_corner = row - (row % 3)
        column_corner = column - (column % 3)
        for i in range(3):
            for j in range(3):
                if grid[row_corner + i][column_corner + j] == number:
                    return False
        return True

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
            if self.is_valid(grid, row, column, number):
                grid[row][column] = number

                if self.solving_sudoku(grid, row, column + 1):
                    return True
            grid[row][column] = 0
        return False

t = Sudoko_Gui()
