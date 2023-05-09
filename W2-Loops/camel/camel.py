camel=input("camelCase: ")
snake = "".join(['_' + n.lower() if n.isupper() else n for i, n in enumerate(camel)])
print("snake_case: "+snake)