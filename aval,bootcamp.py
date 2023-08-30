def is_prime(number, primes):
    for prime in primes:
        if prime * prime > number:
            break
        if number % prime == 0:
            return False
    return True

def generate_primes(limit):
    primes = [2]
    num = 3
    while len(primes) < limit:
        if is_prime(num, primes):
            primes.append(num)
        num += 2
    return primes

def main():
    initial_limit = 50
    prime_list = generate_primes(initial_limit)
    
    print("Prime numbers in the list:", prime_list)

if __name__ == "__main__":
    main()