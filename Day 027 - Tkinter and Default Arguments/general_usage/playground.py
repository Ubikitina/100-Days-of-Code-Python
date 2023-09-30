"""
Playground for unlimited positional arguments
"""

"""
Section 1: Use of *args
"""
# Define a function 'add' that takes an arbitrary number of arguments.
def add(*args):
    # Initialize a variable 'sum' to store the sum of elements.
    total = 0

    # Iterate through each element in the 'args' tuple.
    for element in args:
        # Add the current 'element' to the 'total'.
        total += element

    # Return the calculated sum.
    return total

# Call the 'add' function with multiple arguments.
result = add(5, 6, 7, 8)

# Print the result, which is the sum of the provided arguments.
print(result)

# Call the 'add' function with multiple arguments. This time we will use a different number of arguments.
result = add(6, 7, 8)

# Print the result, which is the sum of the provided arguments.
print(result)


"""
Section 2: Use of **kwargs (key word arguments)
"""
# Define a function 'calculate' that takes an initial value 'n' and keyword arguments (**kwargs).
def calculate(n, **kwargs):
    # print(kwargs) # It is a dictionary

    # Access the 'add' keyword argument from kwargs and add it to 'n'.
    n += kwargs["add"]

    # Access the 'multiply' keyword argument from kwargs and multiply it by 'n'.
    n *= kwargs["multiply"]

    # Return the modified 'n' after performing the specified operations.
    return n

# Call the 'calculate' function with an initial value of 2 and keyword arguments 'add' and 'multiply'.
result = calculate(2, add=3, multiply=5)

# Print the result after applying the operations specified by the keyword arguments.
print(result)

"""
Section 3: A class that uses keyword arguments **kwargs
"""
# Note: This is not the usual way to create classes. However, in the tkinter module, this often happens. This is
# because tkinter was originally programmed in another language, and when it was ported to Python, this was the
# simplest conversion method.
class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # It's better to use .get method instead of doing it the way it was done above, so that the code can skip
        # if there's no such keyword
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

my_car2 = Car(model="GT-R")