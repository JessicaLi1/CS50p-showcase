from tabulate import tabulate
import sys
import csv

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        menu = [row for row in reader]
    print(tabulate(menu, headers='firstrow', tablefmt='grid'))

except FileNotFoundError:
    sys.exit("File does not exist")
