# Number Guessing Game

A beginner-friendly Python guessing game where the player tries to guess a secret number. The program gives hints and counts how many attempts the player needs to find the correct number.

## About the Project

I am a freshman undergraduate learning Python. This project is part of my beginner programming practice and focuses on `while` loops, conditional statements, user input, and counters.

## What the Program Does

The program:

1. Sets a secret number.
2. Asks the player to guess the number.
3. Checks whether the guess is too low or too high.
4. Continues asking for guesses until the correct number is entered.
5. Counts the number of attempts.
6. Displays the final result.

## Concepts Used

- `input()`
- `int()`
- Variables
- `while` loops
- `if / else`
- Comparison operators
- Counters
- f-strings

## Code

```python
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

example:
Guess the number: 4
Too low!
Guess again: 9
Too high!
Guess again: 7
Correct!
You guessed it in 3 attempts.
Requirements
Python 3.x
No external libraries
How to Run

Run the program from a terminal:
python "number guessing game.py"
Then enter your guesses when prompted.

Learning Status

Level: Beginner
Project Type: Python Practice Project
Focus: While loops, conditions, user input, and counters

Future Improvements
Generate a random secret number.
Set a maximum number of attempts.
Add difficulty levels.
Allow the player to restart the game.
Give a score based on the number of attempts.
Add input validation.
Move the game logic into functions.
Author

A freshman undergraduate learning Python and developing programming fundamentals through hands-on projects.
