import random

# generate a random number between 1 to 10
secret_number = random.randint(1, 10)

# maximum attempts allowed
max_attempts = 3

# function to display a welcome message   
def welcome_message():
    print("\nWelcome to the number guessing game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")

# function for recursive guessing
def guess_recursive(attempts_left):
    # get user input
    guess = int(input("\nGuess the number between 1 to 10: "))

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You have guessed the correct number.")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left - 1}")
        if attempts_left > 1:
            # make recursive call for another guess
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")
            welcome_message()
            guess_recursive(max_attempts)

# calling the function
welcome_message()
guess_recursive(max_attempts)
print(f"Memory address of secret number {secret_number} is: {id(secret_number)}")