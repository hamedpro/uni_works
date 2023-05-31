user_input = input()
if(user_input == "a"):
    empty_cells_pattern = []

    for i in range(5):
        empty_cells_pattern.append(4-i)
    for i in range(5):
        if(i != 0):
            empty_cells_pattern.append(i)

    for i in range(len(empty_cells_pattern)):
        print(" "* empty_cells_pattern[i] + "*" * (9-(2* empty_cells_pattern[i])) + " "* empty_cells_pattern[i])
elif user_input == "b":
    for i in range(6):
        if i == 0 :
            print(" "*4 + "*" + " "*4)
        if i%2 != 0:
            print(" "*(int((9-i-2)/2)) +( "*" + i*" " +"*")+ " "*(int((9-i-2)/2)))
    print("*"*9)