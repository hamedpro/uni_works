list1 = eval(input())
list2 = eval(input())
print(sorted((list(filter(lambda x : x in list2, list1)))))
