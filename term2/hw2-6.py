given_list  = eval(input())
print(dict(zip(given_list, (list(map(lambda i : given_list.count(i), given_list))) )))