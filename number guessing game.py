secret_number = 7

guess = int(input("Guess the number: "))
attempts = 1

while guess != secret_number:

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))
    attempts = attempts + 1

print("Correct!")
print(f"You guessed it in {attempts} attempts.")
