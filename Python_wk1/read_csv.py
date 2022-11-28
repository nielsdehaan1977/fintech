"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
import csv
from pathlib import Path

# @TODO: Create a path to the `quarterly_data.csv` file

csvpath = Path('quarterly_data.csv')

with open(csvpath) as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        print(row)
        