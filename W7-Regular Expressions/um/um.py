import re
import sys


def main():
    print(count(input("Input: ")))


def count(s):
    pattern = r"\bum\b"
    regex = re.compile(pattern, re.IGNORECASE)
    return len(regex.findall(s))


if __name__ == "__main__":
    main()
