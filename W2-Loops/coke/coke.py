coins=0

while True:
    rest_due=50-coins
    if rest_due<=0:
        break
    else:
        print(f"Amount Due: {rest_due}")
    coins_in=int(input("Insert Coin: "))
    if coins_in not in [25, 10, 5]:
        coins=coins
    else:
        coins+=coins_in

change=abs(rest_due)
print(f"Change Owed: {change}")