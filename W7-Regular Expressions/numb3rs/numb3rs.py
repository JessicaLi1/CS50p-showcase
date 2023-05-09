import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #split input string by periods and ensure there ar 4 octets
    octets = ip.split(".")
    if len(octets) != 4:
        return False

    #check that each octet is an integer between 0 and 255
    for octet in octets:
        try:
            num = int(octet)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
        
    #if all ostets ar valid, return True
    return True

if __name__ == "__main__":
    main()