import random
import csv

class Person:
    def __init__(self, names_file='Both Names - Sheet1.csv'):
        self.name = self.get_random_name(names_file)

    def get_random_name(self, filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)
            random_row = random.choice(rows)
            random_name = ','.join(random_row)
        return random_name

    
    
    @property
    def nameSelf(self):
        return self.name
    

# Example usage:
# person = Person() 
# print(person.name)
