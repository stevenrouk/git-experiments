"""Some Docstring here."""

def hello_world():
    print("Hello world!")

def primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

if __name__ == '__main__':
    hello_world()
    print(primes(11))

