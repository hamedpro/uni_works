entered_number = int(input())
common_divisors = []
for i in range(1,entered_number +1 ):
    if(entered_number % i == 0 and entered_number != i):
        common_divisors.append(i)
print("True" if sum(common_divisors) == entered_number else "False")