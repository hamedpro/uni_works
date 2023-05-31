user_input = input()
range_start = int(user_input.split(' ')[0])
range_end = int(user_input.split(' ')[1])
for i in range(range_start,range_end +1 ):
    if i % 3 == 0 and i % 5 == 0 :
        print(i)

