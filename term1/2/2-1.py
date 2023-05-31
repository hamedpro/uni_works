user_input = input()
numbers = user_input.split(',') 
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
filtered_numbers = []
for i in range(len(numbers)):
    if(numbers[i] != 0):
        filtered_numbers.append(numbers[i])
result = filtered_numbers.copy()
for i in range(len(numbers)-len(filtered_numbers)):
    result.append(0)
print(result)