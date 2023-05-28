#always x is user and o is computer
import random
state = [] #this variable holds current table fields state
for i in range(1,10):
    state.append(None)
def print_state(state):
    def g(index):
        return index if state[index] == None else state[index]
    print(f'{g(0)}|{g(1)}|{g(2)}')
    print('-----')
    print(f'{g(3)}|{g(4)}|{g(5)}')
    print('-----')
    print(f'{g(6)}|{g(7)}|{g(8)}')
    
def check_state(state):
    # return values : "x"(x is winner), "o", "equal" , "not_finished"
    tmp = [[0,1,2],[0,3,6],[2,5,8],[6,7,8],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
    for i in tmp:
        if((state[i[0]] == state[i[1]] and state[i[1]] == state[i[2]] and state[i[2]] != None)):
            return state[i[0]]
    return "equal" if state.count(None) == 0 else "not_finished"
def simple_ai(state):
    # it returns index of the best field that computer must select
    for i in range(0,9):
        cloned_state = state.copy()
        if(cloned_state[i] == None):
            cloned_state[i] = "o"
            if(check_state(cloned_state) == "o"):
                return i
    for i in range(0,9):
        cloned_state = state.copy()
        if(cloned_state[i] == None):
            cloned_state[i] = "x"
            if(check_state(cloned_state) == "x"):
                return i
    for i in [0,2,6,8,4,1,3,5,7]:
        if(state[i] == None):
            return i
print('starting game ...')
print('you are "x" and playing against computer("o")')
turn = "x" if random.randint(1,100) > 50 else "o"
print(f'this time "{turn}" starts first (it was decided randomly!)')
print_state(state)
while True:
    if(turn == "o"):
        tmp = simple_ai(state)
        state[tmp] = "o"
        print(f'computer decided to select {tmp}')
    elif(turn == "x"):
        tmp = int(input("this is your turn please enter a field number: "))
        if(state[tmp] != None):
            print('field you chose was not empty')
            break
        state[tmp] = "x"
        print(f'user decided to select {tmp}')
    print('state after change:')
    print_state(state)
    print('+++++++++++++++++++++++')
    tmp = check_state(state)
    if(tmp == "x" or tmp == "o"):
        print(f'{tmp} won the game')
        break
    elif (check_state(state) == "equal"):
        print('game finished and no one won')
        break 
    turn = "x" if turn == "o" else "o"