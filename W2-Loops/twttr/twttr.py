original=input("Input: ")
vowels="aeiouAEIOU"
new=original[0]+"".join([char for char in original[1:] if char not in vowels])
print(f"Output: {new}")
