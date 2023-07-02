import random
from tkinter import *
from tkinter import filedialog
class Sudoku:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.solved_grid = None
        self.generate()

    def generate(self):
        self.solve() # solve a complete sudoku puzzle
        count = 81 - self.difficulty
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.grid[row][col] != 0:
                backup = self.grid[row][col]
                self.grid[row][col] = 0
                copy_grid = [row[:] for row in self.grid]
                solutions = self.count_solutions(copy_grid)
                if solutions != 1:
                    self.grid[row][col] = backup
                else:
                    count -= 1

    def set_grid(self, new_grid):
        self.grid = new_grid

    def count_solutions(self, grid):
        # check if the puzzle is already solved
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.count_solutions(grid) != 1:
                                return 2
                            grid[row][col] = 0
                    return 1
        return 1

    def is_valid(self, grid, row, col, num):
        # check if the number is valid in the row
        for i in range(9):
            if grid[row][i] == num:
                return False
        # check if the number is valid in the column
        for i in range(9):
            if grid[i][col] == num:
                return False
        # check if the number is valid in the 3x3 box
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve(self):
        # find an empty cell
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    # try values from 1 to 9
                    for num in range(1, 10):
                        if self.is_valid(self.grid, row, col, num):
                            self.grid[row][col] = num
                            # continue solving recursively
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    # no valid value found
                    return False
        # all cells are filled
        self.solved_grid = [row[:] for row in self.grid]
        return True

class SudokuGUI:
    def __init__(self):
        self.sudoku = Sudoku(30) # default difficulty is easy
        self.root = Tk()
        self.root.title("Sudoku")
        self.entries = []
        self.create_menu()
        self.create_grid()
        self.create_solve_button()
        self.create_solve_user_button()
        self.root.mainloop()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.load_puzzle)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

    def create_grid(self):
        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = Entry(self.root, width=2, font=("Arial", 20), justify=CENTER)
                entry.grid(row=row, column=col, padx=2, pady=2)
                if self.sudoku.grid[row][col] != 0:
                    entry.insert(END, str(self.sudoku.grid[row][col]))
                    entry.config(state=DISABLED)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def create_solve_button(self):
        solve_button = Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=4, pady=10)

    def create_solve_user_button(self):
        solve_button = Button(self.root, text="Check Solution", command=self.check_solution)
        solve_button.grid(row=9, column=5, pady=10)

    def load_puzzle(self):
        filename = filedialog.askopenfilename()
        with open(filename) as f:
            lines = f.readlines()
        new_grid = [[int(char) for char in line.strip()] for line in lines]
        self.sudoku.set_grid(new_grid)
        self.update_grid()

    def solve_puzzle(self):
        self.sudoku.solve()
        self.update_grid()

    def check_solution(self):
        user_grid = [[int(entry.get()) if entry.get() else 0 for entry in row] for row in self.entries]
        if self.check_valid(user_grid):
            if self.check_solution_helper(user_grid, self.sudoku.solved_grid):
                self.show_message("Congratulations, you solved the puzzle!")
            else:
                self.show_message("Sorry, your solution is incorrect.")
        else:
            self.show_message("Invalid input. Please check your entries.")

    def check_valid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    num = grid[row][col]
                    grid[row][col] = 0
                    if not self.sudoku.is_valid(grid, row, col, num):
                        return False
                    grid[row][col] = num
        return True

    def check_solution_helper(self, grid1, grid2):
        for row in range(9):
            for col in range(9):
                if grid1[row][col] != grid2[row][col]:
                    return False
        return True

    def update_grid(self):
        for row in range(9):
            for col in range(9):
                entry = self.entries[row][col]
                entry.delete(0, END)
                if self.sudoku.grid[row][col] != 0:
                    entry.insert(END, str(self.sudoku.grid[row][col]))
                    entry.config(state=DISABLED)
                else:
                    entry.config(state=NORMAL)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    SudokuGUI()