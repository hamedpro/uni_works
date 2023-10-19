import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import copy
class SudokuBackend:
    def print_board(self, board):
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

    def gen_empty_grid(self):
        return [[0 for i in range(9)] for j in range(9)]

    """ difficalty is number of not empty cells """
    def generate(self ,difficulty = 51   ): 
        grid = self.gen_empty_grid()
        grid[random.randint(0,8)][random.randint(0,8)] = random.randint(1,9)
        self.solve(grid)

        count = 81 - difficulty
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if grid[row][col] != 0:
                backup = grid[row][col]
                grid[row][col] = 0
                copy_grid = [row[:] for row in grid]
                solutions = self.count_solutions(copy_grid)
                if solutions != 1:
                    grid[row][col] = backup
                else:
                    count -= 1
        return grid 

    def count_solutions(self, grid):
        # check whether this puzzle is solvable or not 
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.can_be_put(grid, [row, col], num):
                            grid[row][col] = num
                            if self.count_solutions(grid) != 1:
                                return 2
                            grid[row][col] = 0
                    return 1
        return 1

    
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

    def can_be_put(self , board, position, number):
        # in that row and col and cube that position is located in there is not any
        # other cell with number= that number we want to put in this position
        t = copy.deepcopy(board)
        t[position[0]][position[1]] = number
        return self.is_valid(t)
    def solve(self,grid):
        # find an empty cell
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    # try values from 1 to 9
                    for num in range(1, 10):
                        if self.can_be_put(grid,[ row, col], num):
                            grid[row][col] = num
                            # continue solving recursively
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    # no valid value found
                    return False
        return True

class SudokuGUI:
    def __init__(self):
        self.sudoku = SudokuBackend() 
        self.root = Tk()
        self.root.title("Sudoku")
        self.entries = []
        self.create_grid()
        self.grid = self.sudoku.gen_empty_grid()
        self.create_bottom_buttons()
        self.create_difficalty_radio_button()
        self.root.mainloop()
    @property
    def grid(self ):
        t = self.sudoku.gen_empty_grid()
        for row in range(9):
            for col in range(9):
                t[row][col] = int(float(self.entries[row][col].get() or 0 ))
        return t 
    @grid.setter
    def grid(self,new_value ):
        for row in range(9):
            for col in range(9):
                entry = self.entries[row][col]
                entry.delete(0, END)
                entry.insert(END, str(new_value[row][col]))

    def create_bottom_buttons(self):
        self.create_solve_button()
        self.create_check_button()
        self.create_create_button()
        self.create_load_button()
    def create_grid(self):
        self.entries = [[None for i in range(9)] for j in range(9)]
        for row in range(9):
            for col in range(9):
                entry = Entry(self.root, width=2, font=("Arial", 20), justify=CENTER)
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

    #functions to create those four buttons below 
    def create_solve_button(self):
        solve_button = Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=4, pady=10)
    def create_load_button(self):
        load_button = Button(self.root , text="load a board" , command=self.load_puzzle)
        load_button.grid(row = 9 , column = 7 )
    def create_check_button(self):
        solve_button = Button(self.root, text="Check Solution", command=self.check_solution)
        solve_button.grid(row=9, column=5, pady=10)
    def create_create_button(self):
        create_button  = Button(self.root , text="create random grid" , command=self.create_button_onclick)
        create_button.grid(row = 9 , column=  6)

    def create_difficalty_radio_button(self):
        self.radio_button_variable = IntVar(self.root , 51 )
        t = Radiobutton(self.root , value=51 , text = 'easy' , variable= self.radio_button_variable)
        t.grid(row = 10 , column= 1)

        t = Radiobutton(self.root , value=41 , text = 'medium' , variable= self.radio_button_variable)
        t.grid(row = 10 , column= 2)

        t = Radiobutton(self.root , value=31 , text = 'hard' , variable= self.radio_button_variable)
        t.grid(row = 10 , column= 3)

    #button onclick funcs 
    def create_button_onclick(self):
        self.grid = self.sudoku.generate(difficulty= self.radio_button_variable.get())
    def rerender(self):
        self.grid = copy.deepcopy(self.grid)
    def load_puzzle(self):
        filename = filedialog.askopenfilename()
        if filename == "":
            self.show_message("you did not select a file ")
            return 
        with open(filename) as f:
            lines = f.readlines()
        new_grid = [[int(char) for char in line.split(',')] for line in lines]
        self.grid = new_grid
        
    def solve_puzzle(self):
        if self.sudoku.is_valid(self.grid) == False:
            self.show_message('this board is not solveable')
            return 
        t = copy.deepcopy(self.grid)

        self.sudoku.solve(t)
        self.grid = t 
        
    def check_solution(self):
        user_grid = self.grid 
        if self.sudoku.is_valid(user_grid):
            self.show_message("continue! this puzzle can be solved")
        else:
            self.show_message("stop trying. this puzzle is not solvable")

    

    def check_solution_helper(self, grid1, grid2):
        for row in range(9):
            for col in range(9):
                if grid1[row][col] != grid2[row][col]:
                    return False
        return True
        

    def show_message(self, message):
        messagebox.showinfo("Message", message)

#SudokuGUI()

a= SudokuBackend()
t = a.gen_empty_grid()
print(t )