# decorator to call function twice
def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

@doubler
def test():
    print("hello")

test()
