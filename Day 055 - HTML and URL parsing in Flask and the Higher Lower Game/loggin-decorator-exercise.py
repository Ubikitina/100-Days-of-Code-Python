inputs = eval(input())  # eval() creates list for inputs with format: [1,2,3]
# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):  # Define a wrapper function
        called_function_text = f"You called {function.__name__}("
        for arg in args:
            called_function_text += f"{arg}, "
        called_function_text = called_function_text[:-2] + ')'  # Replace the last character with closing parenthesis
        print(called_function_text)

        # The above could be done easier with this code: print(f"You called {function.__name__}{args}")

        print(f"It returned {function(args[0],args[1],args[2])}")
    return wrapper  # Return the wrapper function



# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])
