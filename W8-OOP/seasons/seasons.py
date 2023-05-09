from datetime import date
import sys
import inflect


def main():
    try:
        minutes=find_minutes(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    print(convert_number_to_words(minutes).capitalize(),"minutes")


def find_minutes(in_date):
    birthdate = date.fromisoformat(in_date)
    today = date.today()
    age=today - birthdate
    return int((age).total_seconds()//60)


def convert_number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number,andword="")
    return words


if __name__ == "__main__":
    main()
