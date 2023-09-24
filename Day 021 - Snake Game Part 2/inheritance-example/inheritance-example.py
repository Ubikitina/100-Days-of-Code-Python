# Define a base class called 'Animal.'
class Animal:
    # Constructor method for initializing an instance of 'Animal.'
    def __init__(self):
        # Initialize the 'num_eyes' attribute to 2 for all animals.
        self.num_eyes = 2

    # Method for animals to breathe.
    def breathe(self):
        # Print a message indicating breathing action.
        print("Inhale, exhale.")

# Define a subclass called 'Fish' that inherits from 'Animal.'
class Fish(Animal):
    # Constructor method for initializing an instance of 'Fish.'
    def __init__(self):
        # Call the constructor of the parent class ('Animal') using 'super()'.
        super().__init__()

    # Method specific to fish for swimming.
    def swim(self):
        # Print a message indicating swimming action.
        print("Moving in water.")

    # Override the 'breathe' method from the parent class.
    def breathe(self):
        # Call the 'breathe' method of the parent class ('Animal') using 'super()'.
        super().breathe()
        # Print an additional message indicating breathing underwater.
        print("doing this underwater.")

# Create an instance of the 'Fish' class and assign it to the variable 'nemo.'
nemo = Fish()

# Call the 'swim' method of the 'Fish' class for the 'nemo' instance.
nemo.swim()

# Call the 'breathe' method of the 'Fish' class for the 'nemo' instance.
nemo.breathe()

# Print the 'num_eyes' attribute of the 'nemo' instance, which is inherited from the 'Animal' class.
print(nemo.num_eyes)
