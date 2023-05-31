# "x" is always User and "o" is computer 
import tkinter as tk
import time 
import random
from tkinter import messagebox

class Game:
    def __init__(self):
        self.buttons = []

        # state is where current state of each button is saved  
        # an array of length 9 which its items is either one of them : "x" , "o" , None (not taken)
        self.state = []

        #filling it with Nones 
        for i in range(1,10):
            i = None
            self.state.append(i)

        self.turn = random.choice(['x','o'])
        self.window_construction(self.turn) 
        if self.turn == "o":
            self.computer_make_move()
        self.tkinter_main_window_instance.mainloop()

    def check_state(self , state):
        #possible return values : 
        # "x" or "o" =>  someone has won the game
        # equal => when there is not any empty square but no one is won
        # not_finished => there is at least a square empty 
        win_situations = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
        for win_situation in win_situations:
            if((state[win_situation[0]] == state[win_situation[1]] == state[win_situation[2]] and state[win_situation[2]] != None)):
                return state[win_situation[0]]
        return "equal" if state.count(None) == 0 else "not_finished"

    def simple_ai(self):
        # it returns index of the best field that computer must select

        # if computer can win with just a single move return index of that move
        for i in range(0,9):
            cloned_state = self.state.copy()
            if(cloned_state[i] == None):
                cloned_state[i] = "o"
                if(self.check_state(cloned_state) == "o"):
                    return i

        # if there is a single move which causes user to win return its index
        # so computer selectes that and user winning is blocked 
        for i in range(0,9):
            cloned_state = self.state.copy()
            if(cloned_state[i] == None):
                cloned_state[i] = "x"
                if(self.check_state(cloned_state) == "x"):
                    return i
        
        # else return index of first empty square from these sequence 
        for i in [0,2,6,8,4,1,3,5,7]:
            if(self.state[i] == None):
                return i
    def computer_make_move(self):
        #returns best index that computer must choose according to specs 
        tmp = self.simple_ai()
        self.state[tmp] = "o"
        self.buttons[tmp].config(text='o')
        self.buttons[tmp].config(state = "disabled")
        self.tkinter_main_window_instance.update()
        current_result = self.check_state(self.state)
        if current_result == "o":
            self.finish_game("o")
        elif current_result == "equal":
            self.finish_game(None)
    def finish_game(self,letter):
        messagebox.showinfo(title="game result" , message = f'{letter if (letter == "x"   or letter == "o" ) else "no one"} won !')
        self.reset_game()
    def button_onclick(self,button_index):
        if self.state[button_index] == None:
            self.state[button_index] = "x"
            self.buttons[button_index].config(text = "x")
            self.buttons[button_index].config(state = "disabled")
            
            current_result = self.check_state(self.state)
            if current_result == "x":
                self.finish_game("x")
            elif current_result == "equal":
                self.finish_game(None)
            else : 
                self.computer_make_move()

    def reset_game(self):
        self.tkinter_main_window_instance.destroy()
        self.__init__()

    def window_construction(self , first_turn):
        self.tkinter_main_window_instance = tk.Tk()
        self.tkinter_main_window_instance.title("tic tac toe")
        self.tkinter_main_window_instance.geometry("600x600")
        self.tkinter_main_window_instance.resizable(0,0)
        self.top_frame = tk.Frame(self.tkinter_main_window_instance)
        self.top_frame.pack()
        self.buttons_frame = tk.Frame(self.tkinter_main_window_instance )
        self.buttons_frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.buttons_frame  , text = "-"  , bg = "red", fg = "black" , command = lambda x = i * 3 + j : self.button_onclick(x))
                btn.config(width=4, height=1, font=("None", 30 , "bold"))
                btn.grid(row = i  , column = j , ipadx = 30 , ipady = 30)
                self.buttons.append(btn)

        
        btn_quit = tk.Button(self.tkinter_main_window_instance , fg = "black" , text='quit', command=self.tkinter_main_window_instance.destroy)
        btn_quit.config(width=4, height=1, font=("None", 30, "bold"))
        btn_quit.pack()
        btn_reset = tk.Button(self.tkinter_main_window_instance , fg = "black", text ="reset game" , command = self.reset_game )
        btn_reset.config(width=7, height=1, font=("None", 30 , "bold"))
        btn_reset.pack()
        self.status_label = tk.Label(self.top_frame , text = f"starting letter : {first_turn}" )
        self.status_label.grid(row = 0 , column =0 )

Game()