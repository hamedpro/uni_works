matrix = [list(range(i * 3 , i * 3 + 3)) for i in range(3)]
print("[", end="")
print(matrix[0], end=",\n")
print(matrix[1], end=",\n")
print(matrix[2], end="]\n")

result = [ [i ** 2 for i in row if i % 2 == 0 ] for row in matrix]
print(result)