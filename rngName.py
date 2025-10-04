import csv
import random

with open('/content/Both Names - Sheet1.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Read all rows into a list
    rows = list(csv_reader)
    # Select a random row from the list
    random_row = random.choice(rows)
    print(','.join(random_row))


    