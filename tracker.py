# decorator to track number of times a function is called
def func_counter(method):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1  # every time a function is called, add 1 to the call counter
        return method(*args, **kwargs)

    wrapper.counter = 0
    return wrapper

# test the func_counter()
@func_counter
def spanishGreeting():
    print("Hola amigos")

# run spanishGreeting() 10 times
x = 0
while (x < 10):
    spanishGreeting()
    x += 1

# gets number of times that spnaishGreeting() was run
spanCount = spanishGreeting.counter
print(spanCount)    #prints '10'


