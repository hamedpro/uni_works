user_input = input()
parent_array = eval(user_input)
array_lengths = []
for i in range(len(parent_array)):
    array_lengths.append(len(parent_array[i]))
print((min(array_lengths),max(array_lengths)))