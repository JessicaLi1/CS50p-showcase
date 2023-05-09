items={

}
while True:
    try:
        item = input().strip().upper()
        items[item] = items.get(item, 0) + 1
    except EOFError:
        break
gro_list = ""
for item in sorted(items):
    gro_list += f"{items[item]} {item}\n"
print(gro_list.rstrip())