# Import the PrettyTable module
from prettytable import PrettyTable

# Create an instance of PrettyTable
table = PrettyTable()

# Add a column named "Pokemon Name" and populate it with values
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

# Add a column named "Type" and populate it with values
table.add_column("Type", ["Electric", "Water", "Fire"])

# Print the table with the added columns and data
print(table)

# Change the alignment of the table's content to left
table.align = "l"

# Print the table again with the updated alignment
print(table)
