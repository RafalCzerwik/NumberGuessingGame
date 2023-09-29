import random


def get_user_guess():
    """Get number from user and return it."""
    while True:
        user_guess = input('Guess the number: ')
        if user_guess.isdigit():
            return int(user_guess)
        else:
            print("It's not a number!")

def main():
    """Main game function."""
    guess_number = random.randint(1, 100)
    while True:
        guess = get_user_guess()
        if guess < guess_number:
            print("Too small!")
        elif guess > guess_number:
            print("Too big!")
        else:
            print("You win!!!")
            break


if __name__ == "__main__":
    main()
