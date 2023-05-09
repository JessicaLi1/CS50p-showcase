import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern1 = r"(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)"
    pattern2 = r"(\d{1,2}) (\w{2}) to (\d{1,2}) (\w{2})"

    match = re.match(pattern1,s) or re.match(pattern2,s)
    if not match:
        raise ValueError('Invalid input')

    if match.re.pattern == pattern1:
        h1, m1, ap1, h2, m2, ap2 = match.groups()
    else:
        h1, ap1, h2, ap2 = match.groups()
        m1 = m2 = "00"

    h1, h2 = int(h1), int(h2)
    if h1 == 12:
        h1 = 0
    if ap1 == "PM":
        h1 += 12
    if h2 == 12:
        h2 = 0
    if ap2 == "PM":
        h2 += 12

    if not (0 <= h1 < 24) or not (0 <= h2 < 24) or not (0 <= int(m1) < 60) or not (0 <= int(m2) < 60):
        raise ValueError("Invalid time")

    return f"{h1:02d}:{m1} to {h2:02d}:{m2}"

if __name__ == "__main__":
    main()