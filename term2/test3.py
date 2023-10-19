import random
t = [random.randint(1,9) for i in range(81)]
def print_board(board):
    for index,number  in enumerate(t) :
        print(number , end = "\n" if( (index  + 1) % 9 == 0 ) else ""  )
print_board(t )