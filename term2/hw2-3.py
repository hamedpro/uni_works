from functools import reduce
n = int(input())
print(reduce(lambda x, y: x+[x[-1]+x[-2]], range(n-2), [0, 1]))
