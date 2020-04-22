import math, sys
#import time
#start_time = time.time()
file_name = sys.argv[1]

def IsPrime(n):
    if n>= 1 and n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

with open(file_name) as inputs:
    for input_data in inputs: 
        print(1 if IsPrime(int(input_data)) else 0)

#duration = time.time() - start_time
