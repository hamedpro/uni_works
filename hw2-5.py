given_list = eval(input())
print(list(filter(lambda x : x == x[::-1], given_list)))