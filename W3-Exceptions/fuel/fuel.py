
while True:
    try:
        frac=input("Fraction: ")
        x,y=map(int,frac.split("/"))
        if x>y:
            continue
        percent=round(x/y*100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print('F')
        else:
            print(f"{percent}%")
        break
    except(ValueError, ZeroDivisionError):
        continue