def main():
    original = input("Input: ")
    new = shorten(original)
    print(f"Output: {new}")

def shorten(word):
    vowels = "aeiouAEIOU"
    return word[0] + "".join([char for char in word[1:] if char not in vowels])

if __name__ == "__main__":
    main()