import csv

with open('cookies-and-code/100-level/coding-101/flight-lookup.py') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Flight Number'])