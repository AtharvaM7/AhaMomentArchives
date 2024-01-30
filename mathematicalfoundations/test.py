#find large prime numbers

import math
import random

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def main():
    print(generate_prime_number())

if __name__ == "__main__":
    main()

