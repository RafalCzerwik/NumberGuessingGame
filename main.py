import random


def get_guess_number():
    """Get guess number from input. Check if is int. Can't be a letter/word"""
    while True:
        try:
            guess_number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return guess_number


def main():
    """Main function with our game"""
    print("Welcome in game GUESS THE NUMBER!\n")
    secret_number = random.randint(1, 100)
    user_number = get_guess_number()
    while user_number != secret_number:
        if user_number < secret_number:
            print("Too small!")
        else:
            print("Too big!")
        user_number = get_guess_number()
    print("You win!")


if __name__ == '__main__':
    main()
