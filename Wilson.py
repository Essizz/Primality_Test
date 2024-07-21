def is_prime_wilson(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    # (n-1)!
    factorial = 1
    for i in range(1, n):
        factorial = (factorial * i) % n
     # Wilson's theorem
    return (factorial + 1) % n == 0

while True:
    try:
        num = int(input("Enter a number: "))
        if is_prime_wilson(num):
            print("This is a prime number.")
        else:
            print("This is a composite number.")
    except ValueError:
        print("You entered an invalid number. Please try again.")