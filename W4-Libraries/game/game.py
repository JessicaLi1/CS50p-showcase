import random
while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        continue
num_gen = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0 or guess == n:
            raise ValueError
    except ValueError:
        continue
    if guess < num_gen:
        print("Too small!")
    elif guess > num_gen:
        print("Too large!")
    else:
        print("Just right!")
        break
