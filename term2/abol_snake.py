import tkinter as tk
import random

class SnakeGUI(tk.Tk):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Snake Game")
        self.canvas = tk.Canvas(self.win, width=400, height=440)
        self.canvas.pack()
        self.score_label = tk.Label(self.win ,text="score = 0 " )
        self.score_label.pack()
        self.restartMethod()
        self.gameloop()

    def restartMethod(self):
        self.food=Food("red",self.canvas)
        self.snake=Snake(0,0,"green",self.canvas,self.score_label)
        self.win.bind("<KeyPress>", self.printKeyInfo)

    def printKeyInfo(self, event):
        if event.keysym == "Up":
            if self.snake.direction == "down":
                return 
            self.snake.vx=0
            self.snake.vy=-20
        elif event.keysym == "Down":
            if self.snake.direction == "up":
                return 
            self.snake.vx=0
            self.snake.vy=+20
        elif event.keysym == "Left":
            if self.snake.direction == "right":
                return 
            self.snake.vx=-20
            self.snake.vy=0
        elif event.keysym == "Right":
            if self.snake.direction == "left":
                return 
            self.snake.vx=+20
            self.snake.vy=0
        self.snake.direction = event.keysym.lower()
    def gameloop(self):
        self.food.checkFood(self.snake.move(self.food.x,self.food.y))
        self.snake.gameOver()
        if (self.snake.game_over_flag):
            self.canvas.delete('all')
            self.canvas.create_text(200, 200, fill="blue", font="Times 25 italic bold", text="GameOver!")
            return 
            
            
        self.canvas.after(300, self.gameloop)

class Snake:
    direction = "right"
    def __init__(self,initX,initY,color,canvas,score_label):
        self.score_label = score_label
        self.x=initX
        self.y=initY
        self.color=color
        self.canvas=canvas
        self.segments=[]
        initialRect=self.canvas.create_rectangle(0,0,20,20,fill=self.color)
        self.segments.append(initialRect)
        
        initialRect=self.canvas.create_rectangle(20,20,40,20,fill=self.color)
        self.segments.append(initialRect)

        self.vx=20
        self.vy=0
        self.game_over_flag=False
    def move(self,foodx,foody):
        self.x+=self.vx
        self.y+=self.vy
        self.segments.insert(0,self.canvas.create_rectangle(self.x,self.y,self.x+20,self.y+20,fill=self.color))
        if (self.x==foodx and self.y==foody):
            self.score_label.config(text = f"score = {len (self.segments) -2 }")
            return True
        else:
            last=self.segments.pop(-1)
            self.canvas.delete(last)
            return False

    def gameOver(self):
        if self.direction == "right" and self.x + 20 == 400 or \
            self.direction == "left" and self.x  == 0 or \
            self.direction == "up" and self.y == 0 or  \
            self.direction == "down" and self.y + 20 == 400 :
            self.game_over_flag = True 
        
            
        for val in self.segments[1:]:
            if(self.canvas.coords(val)[0]==self.x and self.canvas.coords(val)[1]==self.y): self.game_over_flag=True
        
class Food:

    def __init__(self,color,canvas):
        self.x = random.randint(1, 19)*20
        self.y = random.randint(1, 19)*20
        self.color=color
        self.canvas=canvas
        self.segments = []
        initialRect = self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20,fill=self.color)
        self.segments.append(initialRect)

    def checkFood(self,wasEaten):
        if (wasEaten):
            self.x = random.randint(1, 19)*20
            self.y = random.randint(1, 19)*20
            self.segments.insert(0, self.canvas.create_oval(self.x, self.y , self.x + 20, self.y + 20,fill=self.color))
            last = self.segments.pop(-1)
            self.canvas.delete(last)


SnakeGUI()
tk.mainloop()