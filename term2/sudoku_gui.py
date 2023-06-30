import tkinter
from sudoku_backend import * 
from tkinter import filedialog
import json 
class GUI:
    @property
    def labels_data(self):
        t = [[] for i in range(9) ]
        for i in range(9):
            for j in range(9):
                t[i].append(self.entry_controlled_variables[i * 9 + j ].get())
        return t 
    @labels_data.setter
    def labels_data(self , new_value ):
        for row in range(9):
            for col in range(9):
                self.entry_controlled_variables[row*9 + col ].set(new_value[row][col])
    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.geometry("500x500")
        self.entry_controlled_variables = [tkinter.IntVar(self.window , 0) for i in range(81)]
        #creating label components 
        self.labels = [ ]
        for i in range(81):
            l = tkinter.Label(self.window)
            cor = self.index_to_cordinates(i)
            
            l.grid(row = cor[0],column=cor[1])
            self.labels.append(l)

        #create difficulty radio buttons
        self.radio_buttons_variable = tkinter.IntVar(self.window,30)
        
        t = tkinter.Radiobutton(self.window,text="easy" , value=30, variable=self.radio_buttons_variable)
        t.grid(row = 10,column=1)
        t = tkinter.Radiobutton(self.window,text="medium" , value=40, variable=self.radio_buttons_variable)
        t.grid(row = 10,column=2)
        t = tkinter.Radiobutton(self.window,text="hard" , value=50, variable=self.radio_buttons_variable)
        t.grid(row = 10,column=3)

        
        #create control menu
        t = tkinter.Button(self.window,text="create",command=self.create)
        t.grid(row = 11,column=1)
        t = tkinter.Button(self.window,text="load",command=self.load)
        t.grid(row = 11,column=2)
        t = tkinter.Button(self.window,text="solve",command=self.solve)
        t.grid(row = 11,column=3)
        t = tkinter.Button(self.window,text="check",command=self.check)
        t.grid(row = 11,column=4)
        self.update()
        self.window.mainloop()
    def load(self):
        filename = filedialog.askopenfilename(title="select a file")
        loaded_board = json.load(open(filename , 'r') )
        self.labels_data= loaded_board
        self.update()
    def create(self):
        self.labels_data =gen_random_board(self.radio_buttons_variable.get())
        self.update()   
    def solve(self):
        solve_board(self.labels_data)
        self.update()
    def check(self):
        if validate_board(self.labels_data) == True :
            tkinter.messagebox.showinfo(title = 'board validation result' , message= 'board is valid')
        else:
            tkinter.messagebox.showerror(title='board validation result' , message= 'board is invalid')
    def index_to_cordinates(self, index):
        return [index // 9, index % 9]

    def update(self):
        for i in range(81):
            cor = self.index_to_cordinates(i)
            self.labels[i].config(text=self.labels_data[cor[0]][cor[1]])

    
        
GUI()