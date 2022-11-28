"""Pathways to Success Part 2."""
# @TODO: Import the csv library
import csv
from pathlib import Path

# @TODO: Create a path to the csv file called `quarterly_data.csv`
csvpath = Path('quarterly_data.csv')

counter = 0
# @TODO: Open the csv path, read the data, and print each row
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        counter = counter + 1
        print("row counter: ", counter)
        print(row) 

