import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not re.match(r'^[a-zA-Z]{2,}',s):
        return False

    if len(s) > 6:
        return False

    if re.match(r'^[a-zA-Z]+0',s):
        return False

    if not re.match(r'^[a-zA-Z]+\d*$',s):
        return False

    return True


main()