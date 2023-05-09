def main():
    while True:
        try:
            frac=input("Fraction: ")
            percent = convert(frac)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        x,y=map(int,fraction.split("/"))
        if y == 0:
            raise ZeroDivisionError
        elif x>y:
            raise ValueError
        percent=round(x/y*100)
        if percent < 0 or percent > 100:
            raise ValueError

    except ValueError:
        raise ValueError
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
