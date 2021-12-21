# Alexander Spurlock
# alexanderspurlock@gmail.com

# test change
import random

user_guesses = []


def play(rand_num):
    print(f"New random number is {rand_num}")  # for testing

    is_valid_input = False
    user_number = 0

    while not is_valid_input:

        try:

            user_number = int(input("Guess a number between 0 and 100: "))
            is_valid_input = True

            user_guesses.append(user_number)

        except ValueError:
            print("NOT VALID INPUT. Please enter another guess")

    if user_number == rand_num and len(user_guesses) == 1:

        first_time_guess()

    else:

        start_guessing(user_number, rand_num)


def start_guessing(user_guess, rand_num):

    is_valid_input = False

    while not is_valid_input:

        try:

            while user_guess != rand_num:

                if user_guess < 0 or user_guess > 100:

                    user_guess = int(input(f"{user_guess} is out of specified range. Try again: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 0 and abs(user_guess - rand_num) <= 5:

                    user_guess = int(input(f"{user_guess} IS BURNING: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 5 and abs(user_guess - rand_num) <= 10:

                    user_guess = int(input(f"{user_guess} is HOT: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 10 and abs(user_guess - rand_num) <= 20:

                    user_guess = int(input(f"{user_guess} is REALLY WARM: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 20 and abs(user_guess - rand_num) <= 30:

                    user_guess = int(input(f"{user_guess} is WARMER: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 30 and abs(user_guess - rand_num) <= 40:

                    user_guess = int(input(f"{user_guess} is WARM: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 40 and abs(user_guess - rand_num) <= 60:

                    user_guess = int(input(f"{user_guess} is COLD: "))
                    user_guesses.append(user_guess)

                elif abs(user_guess - rand_num) > 60 and abs(user_guess - rand_num) <= 100:

                    user_guess = int(input(f"{user_guess} is FREEZING: "))
                    user_guesses.append(user_guess)

                if user_guess == rand_num:

                    response_yes = ["y", "yes", "yeah", "yep"]

                    print("You guessed the right number.")
                    print("It took you " + str(len(user_guesses)) + " tries.")

                    question = input("Would you like to play again? (y, yes, yeah, yep)").lower()

                    if question in response_yes:
                        user_guesses.clear()
                        play(random.randint(0, 101))
                    else:
                        print("Goodbye.")

        except ValueError:
            print("NOT VALID INPUT. Please enter another guess")


def first_time_guess():

    response_yes = ["y", "yes", "yeah", "yep"]

    print("You have guessed the right number on your first try.")
    question = input("Would you like to play again? (y, yes, yeah, yep)").lower()

    if question in response_yes:
        user_guesses.clear()

        print("Okay, let's see if you can get it on your first try again.")
        play(random.randint(0, 101))

    else:
        return print("Goodbye.")


if __name__ == "__main__":
    play(random.randint(0, 101))
