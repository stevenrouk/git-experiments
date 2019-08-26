"""Some Docstring here."""

def hello_world():
    print("Hello world!")

def primes(n):
    primes = []
    for i in range(2, n+1):
        for p in primes:
            if i % p == 0:
                primes.append(i)
                break
    return primes

if __name__ == '__main__':
    hello_world()

