from tkinter import Canvas, Label, Tk
from random import choice

class Common:
    def find_direction(self, cell1 , cell2):
        if(cell1[0] != cell2[0] and cell1[1] != cell2[1]):
            raise "these 2 passed cells can not create a sequence"
        if cell1[0] == cell2[0]:
            if cell1[1] > cell2[1]:
                return "up"
            else:
                return "down"
        else:
            if cell1[0] < cell2[0]:
                return "right"
            else:
                return "left"
    def dry_grow(self, cells):
        #it just returns a new cell in the end of snake tail
        new_cell = [
        ]
        for i in range(2):
            if cells[0][i] == cells[1][i]:
                new_cell.append(cells[0][i]) 
            else :
                direction = self.find_direction(cells[0] , cells[1])
                if(direction == "right" or direction == "down"):
                    new_cell.append(min(cells[0][i], cells[1][i]) - 1)
                else:
                    new_cell.append(max(cells[0][i], cells[1][i])  + 1)
        return new_cell
    def calc_cordinates(self, cells):
        tmp = []
        for cell in cells:
            tmp.append(
                [
                    20 * (cell[0] - 1),
                    20 * (cell[1] - 1),
                    20 * (cell[0]),
                    20 * (cell[1]),
                ]
            )
        return tmp 
class Snake(Common):
    # array of tuples (x , y) (not like math)
    # top left is 1,1
    #  order is considered : last one is head
    cells = [[1, 1], [2, 1]]
    direction = "right"

    def __init__(self, canvas, food, score_up):
        self.canvas = canvas
        self.rerender_snake()
        self.food = food
        self.score_up = score_up

    def grow(self):
        self.cells.insert(0, self.dry_grow(self.cells))
        self.rerender_snake()

    def rerender_snake(self):
        self.canvas.delete("snake")
        for cord in self.cords:
            self.canvas.create_rectangle(*cord, fill="blue", tag="snake")

    @property
    def cords(self):
        return self.calc_cordinates(self.cells)

    def move(self):
        # direction is either up , down , left or right
        head = self.cells[-1]
        if self.direction == "up":
            next_cell = [head[0], head[1] - 1]
        elif self.direction == "down":
            next_cell = [head[0], head[1] + 1]
        elif self.direction == "right":
            next_cell = [head[0] + 1, head[1]]
        elif self.direction == "left":
            next_cell = [head[0] - 1, head[1]]
        self.cells.pop(0)
        self.cells.append(next_cell)
        self.rerender_snake()
        self.canvas.update()
        if self.food.cords == next_cell:
            self.score_up()
            self.grow()
        if (
            (next_cell[0] < 1 or next_cell[0] > 10)
            or (next_cell[1] < 1 or next_cell[1] > 10)
            or (self.cells.count(next_cell) == 2)
        ):
            self.canvas.delete("all")
            self.canvas.create_text(100, 100, text="game over")
        else:
            self.canvas.after(300, self.move)


class Food(Common):
    def __init__(self, canvas):
        self.canvas = canvas
        self.rerender()

    def rerender(self):
        self.canvas.delete("food")
        self.cords = [choice(list(range(1, 11))) for i in range(2)]
        self.canvas.create_rectangle(*self.calc_cordinates([self.cords])[0], tag="food")


class Game(Common):
    score = 0

    def createCanvas(self):
        self.window = Tk()
        self.window.geometry("250x250")

        self.score_label = Label(self.window, text="score is 0")
        self.score_label.grid(row=1, column=1)

        self.canvas = Canvas(self.window, width=200, height=200, bg="red")
        self.canvas.grid(row=2, column=1)

    def change_snake_direction(self, new_direction):
        conflict_situations = [["down", "up"], ["left", "right"]]
        for situation in conflict_situations:
            tmp = [self.snake.direction, new_direction]
            if tmp == situation or list(reversed(tmp)) == situation:
                return
        self.snake.direction = new_direction

    def score_up(self):
        self.food.rerender()
        self.score += 1
        self.score_label.config(text=f"score is {self.score }")

    def __init__(self):
        self.createCanvas()
        self.food = Food(self.canvas)
        self.snake = Snake(self.canvas, self.food, self.score_up)
        # snake.grow()
        self.snake.move()
        self.window.bind("<Left>", lambda x: self.change_snake_direction("left"))
        self.window.bind("<Up>", lambda x: self.change_snake_direction("up"))
        self.window.bind("<Right>", lambda x: self.change_snake_direction("right"))
        self.window.bind("<Down>", lambda x: self.change_snake_direction("down"))
        self.window.mainloop()


Game()
