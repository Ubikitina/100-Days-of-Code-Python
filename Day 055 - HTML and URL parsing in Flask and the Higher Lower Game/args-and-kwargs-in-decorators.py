## Advanced Python Decorator Functions

# Define a User class with an __init__ method to initialize a user object with a name and a default login status
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Define a decorator function named is_authenticated_decorator that checks if the user is logged in
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):  # Define a wrapper function
        if args[0].is_logged_in == True:  # Check if the user is logged in. User is passed as args[0]
            function(args[0])  # Call the original function if the user is logged in
    return wrapper  # Return the wrapper function

@is_authenticated_decorator  # Apply the is_authenticated_decorator to the create_blog_post function
def create_blog_post(user):
    # Print a message indicating the creation of a new blog post for the specified user
    print(f"This is {user.name}'s new blog post.")

# Create a new User instance named "angela"
new_user = User("angela")
new_user.is_logged_in = True  # Set the login status of the user to True

# Call the create_blog_post function with the new_user as an argument args[0]
create_blog_post(new_user)