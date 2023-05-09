import validators


def main():
    user_in = input("What's your email address? ")
    if validators.email(user_in):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()