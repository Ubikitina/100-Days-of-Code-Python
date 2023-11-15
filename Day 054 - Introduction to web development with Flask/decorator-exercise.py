import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):  # This is the decorator
    def wrapper_function():
        # Do something before the function
        start_time = time.time()
        function()
        # Do something after the function
        end_time = time.time()
        difference = end_time - start_time
        print(f"{function.__name__} run speed: {difference}")
    return wrapper_function # It is necessary to return something so that the decorator works

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()