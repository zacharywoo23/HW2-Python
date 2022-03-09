import time

# decorator to calculate time to run a function
def calculate_time(func):
    def wrapper():
        time_start = time.time()    #time right before function starts
        func()
        time_end = time.time()      #time right after function ends
        timeToRun = time_end - time_start
        print("Seconds to run")
        print(timeToRun)
    return wrapper

@calculate_time
def test():
    i = 10000000
    while i > 0:
        i -= 1

test()
