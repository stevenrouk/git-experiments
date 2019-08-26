"""Some Docstring here."""

def hello_world():
    print("Hello world!")

def generator_function(n):
    for i in list(range(n)):
        yield i

if __name__ == '__main__':
    hello_world()

