# getting input from user
user_input = []
while True:
    tmp = input()
    if(tmp == " "):
        break
    else:
        user_input.append(tmp)
# parsed_user_input = this variable should be something like [("a",22),("a",23),("b",24)]
parsed_user_input = []
for i in range(len(user_input)):
    tmp = user_input[i].split(":")
    parsed_user_input.append((tmp[0].strip(),int(tmp[1].strip())))
def find_unique_items(array):
    result = []
    for i in range(len(array)):
        if(not(array[i] in result)):
            result.append(array[i])
    return result
keys = []
for i in range(len(parsed_user_input)):
    keys.append(parsed_user_input[i][0])
keys = find_unique_items(keys)
result = {}
for i in range(len(keys)):
    result[keys[i]] = []
for i in range(len(parsed_user_input)):
    result[parsed_user_input[i][0]].append(parsed_user_input[i][1])
def sort_by_keys(dct: dict) -> dict:
    return {k: dct[k] for k in sorted(dct.keys())}
print(sort_by_keys(result))