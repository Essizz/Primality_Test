import random
from math import gcd

def power(a, n, p):
    # Initialize result
    res = 1
    # Update 'a' if 'a' >= p
    a = a % p
    while n > 0:
        # If n is odd, multiply 'a' with result
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            # n must be even now
            n = n // 2
    return res % p

def isPrime(n, k):
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    # Try k times
    else:
        for i in range(k):
            # Pick a random number in [2..n-2]
            # Above corner cases make sure that n > 4
            a = random.randint(2, n - 2)
            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False
    return True
def isCarmichaelNumber(n):
    # Carmichael numbers are composite numbers
    if isPrime(n, 5) or n < 2:
        return False
    b = 2
    while b < n:
        # If "b" is relatively prime to n
        if gcd(b, n) == 1:
            # And pow(b, n-1) % n is not 1, return False.
            if power(b, n - 1, n) != 1:
                return False
        b = b + 1
    return True

user_input = int(input("Enter a number: "))

if isCarmichaelNumber(user_input):
    print(f"{user_input} is a Carmichael number.")
elif isPrime(user_input, 5):
    print(f"{user_input} is a probably prime number.")
else:
    print(f"{user_input} is a composite number.")