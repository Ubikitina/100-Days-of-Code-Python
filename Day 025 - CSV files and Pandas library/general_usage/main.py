"""
======================
This is the previous way to read files
======================
"""

with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)

"""
======================
Here's how to read files using the csv library
======================
"""

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


"""
======================
Now we will see how to use the pandas library
======================
"""
import pandas

# We can directly read a CSV
data = pandas.read_csv("weather_data.csv")
print(data)  # The table is printed in a proper format
print(type(data))  # The whole table is a DataFrame
print(data["temp"])  # We can print a column by indicating its name
print(type(data["temp"]))  # Each column is a Series

# We can convert the data (a DataFrame) to a dictionary
data_dict = data.to_dict()
print(data_dict)

# We can convert a column (a Series) to a list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculate the average of a Series - temperature column
print(data["temp"].mean())

# Maximum
print(data["temp"].max())

# Another way to access the columns
print(data["condition"])
print(data.condition)  # This gets the same result as the line before

# Get data in a Row
monday = data[data.day == "Monday"]
print(monday)
print(monday.condition)
print(data[data.temp == data.temp.max()])  # Get the whole row where the temperature was the maximum temperature.

# Create a dataframe from scratch
data_dict = {  # This is the dictionary that we want to convert into a DataFrame
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # Just by creating the DataFrame like this is enough
print(data)  # The data now looks like a table
data.to_csv("new_data.csv")  # We will create a new csv file by using the data above

"""
======================
Exercises by using 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv file
======================
"""
# Read the CSV file into a DataFrame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Use the value_counts() method to calculate the counts of unique values in the "Primary Fur Color" column
color_counts = data["Primary Fur Color"].value_counts()

# Create a new CSV file with the count
color_counts.to_csv("count.csv")