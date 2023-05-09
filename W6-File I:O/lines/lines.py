import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename, "r") as file:
        code_lines = 0
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            code_lines += 1
    print(f"{filename} has {code_lines} lines of code.")
except FileNotFoundError:
    sys.exit("File does not exist")