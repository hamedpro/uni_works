def find_direction(cell1 , cell2):
    if(cell1[0] != cell2[0] and cell1[1] != cell2[1]):
        raise "these 2 passed cells can not create a sequence"
    if cell1[0] == cell2[0]:
        if cell1[1] > cell2[1]:
            return "up"
        else:
            return "down"
    else:
        if cell1[0] < cell2[0]:
            return "right"
        else:
            return "left"
def dry_grow(cells):
    #it just returns a new cell in the end of snake tail
    new_cell = [
    ]
    for i in range(2):
        if cells[0][i] == cells[1][i]:
            new_cell.append(cells[0][i]) 
        else :
            direction = find_direction(cells[0] , cells[1])
            if(direction == "right" or direction == "down"):
                new_cell.append(min(cells[0][i], cells[1][i]) - 1)
            else:
                new_cell.append(max(cells[0][i], cells[1][i])  + 1)
    return new_cell
def calc_cordinates(cells):
    tmp = []
    for cell in cells:
        tmp.append(
            [
                20 * (cell[0] - 1),
                20 * (cell[1] - 1),
                20 * (cell[0]),
                20 * (cell[1]),
            ]
        )
    return tmp 