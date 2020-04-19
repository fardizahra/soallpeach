import math, sys
import time
start_time = time.time()
def IsPrime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

with open("input.txt") as inputs:
    with open('expected.txt', 'w') as outfile:
        for input_data in inputs: 
            print(1 if IsPrime(int(input_data)) else 0, file = outfile)
        outfile.close()

duration = time.time() - start_time
print(duration)
