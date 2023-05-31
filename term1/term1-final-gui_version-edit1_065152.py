#x is always user and o is always computer 
import tkinter as tk
import random
from tkinter.messagebox import showinfo

def check_state(state,dry_run=False):
    tmp = [[0,1,2],[0,3,6],[2,5,8],[6,7,8],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
    for i in tmp:
        if(state[i[0]] == state[i[1]] and state[i[1]] == state[i[2]] and state[i[2]] != ""):
            if not dry_run:
                finish_game(state[i[0]])
            return state[i[0]]
    if(state.count("") == 0):
        if not dry_run:
            finish_game('equal')
        return "equal"
    else:
        return "not_finished"
def simple_ai(state):
    # it returns index of the best field that computer must select
    for i in range(0,9):
        cloned_state = state.copy()
        if(cloned_state[i] == ""):
            cloned_state[i] = "o"
            if(check_state(cloned_state,dry_run=True) == "o"):
                return i
    for i in range(0,9):
        cloned_state = state.copy()
        if(cloned_state[i] == ""):
            cloned_state[i] = "x"
            if(check_state(cloned_state,dry_run=True) == "x"):
                return i
    for i in [0,2,6,8,4,1,3,5,7]:
        if(state[i] == ""):
            return i

window=tk.Tk()
window.title('بازی دوز')
global turn ,result,player_points , buttons
result=['','','','','','','','','']
player_points=[0,0] # with order : user(x) , computer(o) 

def select(selector,index):
    global turn, result
    if result[index]=='':
        result[index]=selector
        buttons[index]['background']= "red" if selector == 'x' else "green"
        buttons[index]['fg']='white'    
        buttons[index]['text']= selector
        #buttons[index]['state']=tk.DISABLED
def button_onclick(button_index):
    global turn, result
    select("x",button_index)
    if(check_state(result) == "not_finished"):
        select("o",simple_ai(result))
        check_state(result)
def reset():    
    global result , turn
    result=['', '' ,'', '' ,'' ,'', '','' ,'']       
    turn='x'  
    points()
    board()
def finish_game(mode):
    if mode == 'x':
        player_points[0]+=1
        showinfo('game result' , 'you won')
        reset()
    elif mode == "o":
        player_points[1]+=1
        showinfo('game result' ,  'computer won')
        reset()
    elif mode == "equal":
        showinfo('result',"game finished but no one won")
        reset()
def points():
    board_frame= tk.Frame(window)
    board_frame.grid(row=0)
    lable_player1=tk.Label(board_frame , text= 'user' , font=('Aviny',16),padx=10)
    lable_player2=tk.Label(board_frame,text='computer',font=('Aviny' ,16),padx=10)

    lable_player1.grid(row=0 , column=0)
    lable_player2.grid(row=0 , column=2)

    point_frame=tk.Frame(window)
    point_frame.grid(row=1)
    point_player_one=tk.Label(point_frame , text=player_points[0], padx=20 ,font=('lalezar' ,18))
    point_player_two=tk.Label(point_frame , text=player_points[1], padx=20 ,font=('lalezar' ,18))
    point_player_one.grid(row=0 , column=0)
    point_player_two.grid(row=0 , column=1)
def board(): 
    global buttons , turn
    buttons=[]
    counter=0
    board_frame=tk.Frame(window)
    board_frame.grid(row=2)
    for row in range(1,4):
        for column in range(1,4):
            index=counter
            buttons.append(index)
            buttons[index]=tk.Button(board_frame , text= '?',command= lambda x = row :button_onclick(x))
            buttons[index].config(width=10 , height=4 ,font=('None' ,18, 'bold'))
            buttons[index].grid(row=row ,column=column)
            counter+=1
points()
board()
    
first_turn = "o" if random.randint(1,100) > 50 else "x"
if first_turn == "o":
    select("o",simple_ai(result))
showinfo('who starts first',f'this time who begins is {first_turn}')

window.mainloop()