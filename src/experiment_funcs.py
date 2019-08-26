"""Some Docstring here."""

def hello_world():
    return "Hello world!"

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

def generator_function(n):
    for i in list(range(n)):
        yield i

if __name__ == '__main__':
    print(hello_world())
    print(primes(11))

