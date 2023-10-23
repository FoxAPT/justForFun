#Prime Number Checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # Once we find a divisor, we can break out of the loop to save time
    print("\n")
    if is_prime:
        print("It's a prime number.")
    else:
        print("It is not a prime number.")
            
n = int(input("Check this number: "))
prime_checker(number=n)

