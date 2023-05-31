user_input = input()
parent_array = eval(user_input)
def algo(array):
    array_lengths = []
    def rec(array):
        result = []
        for i in range(len(array)):
            if type(array[i]) is list:
                array_lengths.append(len(array[i]))
                tmp = rec(array[i])
                for j in range(len(tmp)):
                    result.append(tmp[j])
            else:
                result.append(array[i])
        return result
    rec(array)
    return (min(array_lengths),max(array_lengths))
print(algo(parent_array))