n = int(input())
def is_prime(number):
    for i in range(1,number ):
        if(number % i == 0 and i != 1 ):
            return False 
    return True 
print([i for i in range(2,n) if is_prime(i)])