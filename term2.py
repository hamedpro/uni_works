import tkinter
import random
class HumanPlayer():
    letter = "X"
class ComputerPlayer():
    letter = "O"
class Board():
    state = [None for i in range(9)]
    buttons = []
    turn = "x" if random.randint(0,100) > 50 else "o"
    def check_state(self):
        # return values : "x"(x is winner), "o", "equal" , "not_finished"
        tmp = [[0,1,2],[0,3,6],[2,5,8],[6,7,8],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
        for i in tmp:
            if((self.state[i[0]] == self.state[i[1]] and self.state[i[1]] == self.state[i[2]] and self.state[i[2]] != None)):
                return self.state[i[0]]
        return "equal" if self.state.count(None) == 0 else "not_finished"
    def simple_ai(self):
        # it returns index of the best field that computer must select
        for i in range(0,9):
            cloned_state = self.state.copy()
            if(cloned_state[i] == None):
                cloned_state[i] = "o"
                if(check_state(cloned_state) == "o"):
                    return i
        for i in range(0,9):
            cloned_state = self.state.copy()
            if(cloned_state[i] == None):
                cloned_state[i] = "x"
                if(check_state(cloned_state) == "x"):
                    return i
        for i in [0,2,6,8,4,1,3,5,7]:
            if(self.state[i] == None):
                return i

    def button_onclick_handler(self,index):
        self.state[index] = "x"
        print(str(index) + " was clicked")
    def __init__(self):
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()

        self.window = tkinter.Tk()
        self.window.title('tic tac toe')
        self.window.geometry('500x500')
        self.window.resizable(False,False)
        for row in range(3):
            for col in range(3):
                button = tkinter.Button(self.window, bg="red",text=row * 3 + col , fg = "white" , command= lambda x =(row * 3 + col):self.button_onclick_handler(x) ,  width=10 , height=4
                )
                button.grid(row=row , column=col)
                self.buttons.append(button)
        self.window.mainloop()
Board()

