#this program reads data from a CSV file and prints it to the console.

import csv

def read_and_print_csv(file_path):
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(', '.join(row))

file_path = 'example.csv'  
read_and_print_csv(file_path)


