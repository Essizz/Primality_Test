import decimal
import numpy as np
from scipy.optimize import minimize_scalar

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    i = n
    while True:
        i += 1
        if is_prime(i):
            return i

def calculate_f_n_within_range(lower_limit, upper_limit, decdig):
    decimal.setcontext(decimal.Context(prec=decdig+2))
    qlim = decimal.Decimal(0.1) ** (decdig+3)
    c = decimal.Decimal(0)
    denominator = 1
    p = 2
    while True:
        q = (p - 1) / decimal.Decimal(denominator)
        if q < qlim:
            break
        c += q
        denominator *= p
        p = next_prime(p)
    c = round(c, decdig)
    
    f_n = c
  
    prime_count = 1
    while True:
        if lower_limit <= prime_count <= upper_limit:
            yield f_n
        if prime_count >= upper_limit:
            break
        f_n = int(f_n) * (f_n - int(f_n) + 1)
        prime_count += 1

def lower_bound_equation(n, p_n):
    return n * (np.log(n) + np.log(np.log(n)) - 3/2) - p_n

def upper_bound_equation(n, p_n):
    return n * (np.log(n) + np.log(np.log(n)) - 1/2) - p_n

def objective_function(n, p_n):
    return abs(lower_bound_equation(n, p_n)), abs(upper_bound_equation(n, p_n))

def find_n_bounds(p_n):
    result_upper = minimize_scalar(lambda n: objective_function(n, p_n)[0], bounds=(2, 2 * p_n), method='bounded')
    result_lower = minimize_scalar(lambda n: objective_function(n, p_n)[1], bounds=(2, 2 * p_n), method='bounded')
    return result_lower.x, result_upper.x

def main():
    decdig = 10000
    prime_number = int(input("Enter a prime number: "))
        
    n_lower, _ = find_n_bounds(prime_number)
    _, n_upper = find_n_bounds(prime_number)
    print("Range n for number" f" {prime_number}")
    print(f"Lower Bound: {int(n_lower)}")
    print(f"Upper Bound: {int(n_upper)}\n")
    print("f_n terms between nth primes:  " f"{n_lower}. and {n_upper}. are f_n terms between primes:\n")
    
    for i, f_n in enumerate(calculate_f_n_within_range(int(n_lower), int(n_upper - 2), decdig), start= int(n_lower )):
        print(f"f_{i} = {f_n}")

    for i, f_n in enumerate(calculate_f_n_within_range(int(n_lower), int(n_upper - 2), decdig), start=int(n_lower )):
        integer_part = int(f_n)  
        if integer_part == prime_number:
            print(f"{prime_number} =" ""f" f_{i}") 
            print(f"{prime_number}" " IS PRIME.")

        elif not is_prime(prime_number):
            print(F"{prime_number} IS COMPOSİTE.")   
       
if __name__ == "__main__":
    main()