names=[]

while True:
    try:
        name=input("Name: ")
        names.append(name)
    except EOFError:
        break

n=len(names)
if n==1:
    print(f'\nAdieu, adieu, to {names[0]}')
elif n==2:
    print(f'\nAdieu, adieu, to {names[0]} and {names[1]}')
else:
    names[-1]='and '+names[-1]
    print(f'\nAdieu, adieu, to {", ".join(names[:-1])}, {names[-1]}')