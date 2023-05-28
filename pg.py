def change_snake_direction(old_direction ,new_direction ):
    conflict_situations = [['down','up'] , ['left','right']]
    for situation in conflict_situations:
        tmp = [old_direction , new_direction]
        if(tmp == situation or reversed(tmp) == situation):
            return 
    print('ok')
change_snake_direction("up", "down")