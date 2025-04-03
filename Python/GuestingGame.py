# Python number guessing game
import random

lower_num = 1
highest_num = 100
guesses = 0
is_running = True

# Generate a random number between lower_num and highest_num
answer = random.randint(lower_num, highest_num)

print("Welcome to the number guessing game!")
print(f"Guess a number between {lower_num} and {highest_num}.")
while is_running:
    guess = input("Enter your guess number: ")
    # Check if the input is a number
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lower_num or guess > highest_num:
            print(f"That number is out of range.")
            print(
                f"Please select a number between {lower_num} and {highest_num}.")
        elif guess < answer:
            print("Your guess is too low. Try again!!")
        elif guess > answer:
            print("Your guess is too high. Try again!!")
        else:
            print(
                f"Congratulations! You guessed the number {answer} in {guesses} tries.")
            is_running = False

    else:
        print("Invalid number.")
        print(f"Please select a number between {lower_num} and {highest_num}.")
