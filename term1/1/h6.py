user_input = input()
m = int(user_input.split(' ')[0])
n = int(user_input.split(' ')[1])

factors_of_m = []
factors_of_n = []

for i in range(1,m+1):
    if(m% i ==0 ):
        factors_of_m.append(i)

for i in range(1,n+1):
    if(n% i ==0 ):
        factors_of_n.append(i)

def find_commons(array1,array2):
    commons = []
    for i in range(len(array1)):
        if(array1[i] in array2):
            commons.append(array1[i])
    return commons
common_factors = find_commons(factors_of_m,factors_of_n)
print(max(common_factors))