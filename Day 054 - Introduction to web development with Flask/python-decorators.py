# In Python, a decorator is a design pattern and a special type of function that is used to modify the behavior of
# another function or method. Decorators are often applied to functions using the @decorator_name syntax, where
# decorator_name is the name of the decorator function.
# To understand the decorators, we will first review some concepts and then tackle the decorators.

# ---------------------------------------------------------------------------------
# Functions have these three components: inputs / functionality / output
# ---------------------------------------------------------------------------------
def add(n1, n2):
    return n1+n2

def substract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1 / n2


# ---------------------------------------------------------------------------------
# First-class objects, can be passed around as arguments e.g. int/string/float etc.
# Functions are first-class objects.
# ---------------------------------------------------------------------------------
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 5, 3)  # In this case, we are passing the function name (first-class object) as argument
print(result)


# ---------------------------------------------------------------------------------
# Nested Functions: functions can be nested inside other functions
# ---------------------------------------------------------------------------------
def outer_function():
    print("I'm outer!")

    # The scope of this inner function is only in the outer_function, we can only call it from the outer_function.
    def nested_function():
        print("I'm inner!")

    nested_function()

outer_function()


# ---------------------------------------------------------------------------------
# Functions can be returned from other functions
# ---------------------------------------------------------------------------------
def outer_function():
    print("I'm outer!2")

    def nested_function():
        print("I'm inner!2")

    return nested_function  # We are returning this inner function

inner_function = outer_function()  # We save the returned function in a variable
inner_function()  # Now we run it


# ---------------------------------------------------------------------------------
# Python Decorator Function
# ---------------------------------------------------------------------------------

# Decorator function example
def decorator_function(function):  # This decorator_function receives a function
    def wrapper_function():
        function()
    return wrapper_function # And returns another function

# When is this decorator function useful? Well, if we have three functions like the ones below, and we want to
# add a delay of 2 seconds before each of them is executed, we could use the decorator.
def say_hello():
    print("Hello!")

def say_bye():
    print("Bye!")

def say_greeting():
    print("How are you?")

# Use of decorator to have a delay before executing the 3 functions above.
# First of all, let's define our decorator:
import time

def delay_decorator(function):
    def wrapper_function():
        # Do something before the function
        time.sleep(2)  # We will pause the execution for 2 seconds before the function
        function()
        # We could also add some code here to execute something else after the function
    return wrapper_function # It is necessary to return something so that the decorator works

# Now, let's add the decorator to each of the functions
@delay_decorator
def say_hello():
    print("Hello!")
@delay_decorator
def say_bye():
    print("Bye!")
@delay_decorator
def say_greeting():
    print("How are you?")

say_hello()
say_greeting()
say_bye()

# Using the @ sign is using syntactic sugar. It is like simplifying the syntax.
# But we could write the same in another way too, for example, for say_greeting this would be:
decorated_function = delay_decorator(say_greeting)  # It is like building a new function by using the other function
decorated_function()  # And later on, running it.
