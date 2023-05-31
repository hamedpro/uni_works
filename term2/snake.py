from tkinter import Canvas, Label, Tk
from utils import dry_grow, calc_cordinates
from random import choice


class Snake:
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
        self.cells.insert(0, dry_grow(self.cells))
        self.rerender_snake()

    def rerender_snake(self):
        self.canvas.delete("snake")
        for cord in self.cords:
            self.canvas.create_rectangle(*cord, fill="blue", tag="snake")

    @property
    def cords(self):
        return calc_cordinates(self.cells)

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


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.rerender()

    def rerender(self):
        self.canvas.delete("food")
        self.cords = [choice(list(range(1, 11))) for i in range(2)]
        self.canvas.create_rectangle(*calc_cordinates([self.cords])[0], tag="food")


class Game:
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
