import sys
import csv

# Check that the correct number of command-line arguments were provided
if len(sys.argv) != 3:
    sys.exit("Wrong argument numbers")

# Try to open the input file
try:
    with open(sys.argv[1], 'r', newline='') as infile:
        reader = csv.reader(infile)
        # Skip the header row
        next(reader)
        # Loop through the rest of the rows and split the name into first and last
        rows = []
        for row in reader:
            name = row[0].strip('"')
            last, first = name.split(', ')
            house = row[1]
            rows.append([first, last, house])

except FileNotFoundError:
    sys.exit("Error: Could not find input file")

# Write the output file
try:
    with open(sys.argv[2], 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header row
        writer.writerow(['first', 'last', 'house'])
        # Write the rest of the rows
        writer.writerows(rows)

except:
    sys.exit("Error: Could not write output file")