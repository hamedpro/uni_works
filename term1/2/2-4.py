
# user_input = "[('v', 8), ('l', 3), ('l', 4), ('W', 4), ('A', 9), ('w', 4), ('h', 5), ('c', 6), ('W', 7), ('e', 1)]"
# user_input = "[('v', 8), ('l', 3), ('l', 4, 8, 0)]"
user_input = input()
parsed_user_input = eval(user_input)



result = []
for i in range(len(parsed_user_input)):
    tmp = []
    [parsed_user_input[i][0],parsed_user_input[i][1]]
    for j in range(len(parsed_user_input[i])):
        tmp.append(parsed_user_input[i][j])
    result.append(tmp)
print(result)


