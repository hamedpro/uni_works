import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 5])
list1 = [a, b]
list2 = [b]
#print([i for i in list1 if (i not in list2)])
print(np.array([1,2]) == np.array([1,2]))

#print([b in list1])