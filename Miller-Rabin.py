import random
from math import gcd

def power(a, n, p):
    # Calculate (a^n) % p using iterative method
    res = 1
    a = a % p  # Update 'a' if 'a' >= p
    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
    return res % p

def is_prime(n, k):
    # Miller-Rabin primality test
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0 or n == 1:
        return False  # Exclude even numbers and 1

    # Write n as 2^r * s + 1 with s odd (by factoring out powers of 2 from (n - 1)
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = power(a, s, n)  # Compute a^s % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)  # Square x
            
            if x == n - 1:
                break
        else:
            return False  # Composite
    return True  # Probably prime

def is_carmichael_number(n):
    # Carmichael numbers must be composite
    if is_prime(n, 5) or n < 2:
        return False

    for b in range(2, n):
        if gcd(b, n) == 1:  # b is relatively prime to n
            if power(b, n - 1, n) != 1:
                return False
    return True

user_input = int(input("Enter a number: "))

if is_carmichael_number(user_input):
    print(f"{user_input} is a Carmichael number.")
elif is_prime(user_input, 5):
    print(f"{user_input} is a probably prime number.")
else:
    print(f"{user_input} is a composite number.")