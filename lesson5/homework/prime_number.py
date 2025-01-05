import math

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            return False 
    return True  

n = int(input("Natural son kiriting: "))
result = is_prime(n)
print(result)