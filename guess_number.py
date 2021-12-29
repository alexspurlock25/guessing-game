# Alexander Spurlock
import random

random_num = random.randint(0, 101)

def play(rand_num:int):
    # for testing - comment out when needed
    print(f"New random number is {rand_num}")

    try:
        user_num = int(input("Guess a number between 0 and 100: "))
        check_guess(user_num, rand_num)

    except ValueError:
        print("NOT VALID INPUT.")
        play(rand_num)


def check_guess(guess, rand_num):
    is_right = False

    while is_right == False:
        if guess < 0 or guess > 100:
            guess = int(input(f"{guess} is out of specified range. Try again: "))

        elif abs(guess - rand_num) > 0 and abs(guess - rand_num) <= 5:
            guess = int(input(f"{guess} IS BURNING: "))

        elif abs(guess - rand_num) > 5 and abs(guess - rand_num) <= 10:
            guess = int(input(f"{guess} is HOT: "))

        elif abs(guess - rand_num) > 10 and abs(guess - rand_num) <= 20:
            guess = int(input(f"{guess} is REALLY WARM: "))

        elif abs(guess - rand_num) > 20 and abs(guess - rand_num) <= 30:
            guess = int(input(f"{guess} is WARMER: "))

        elif abs(guess - rand_num) > 30 and abs(guess - rand_num) <= 40:
            guess = int(input(f"{guess} is WARM: "))

        elif abs(guess - rand_num) > 40 and abs(guess - rand_num) <= 60:
            guess = int(input(f"{guess} is COLD: "))

        elif abs(guess - rand_num) > 60 and abs(guess - rand_num) <= 100:
            guess = int(input(f"{guess} is FREEZING: "))

        if guess == rand_num:
            is_right = True

            response_yes = ["y", "yes", "yeah", "yep"]
            print("You guessed the right number.")
            question = input("Would you like to play again? (y, yes, yeah, yep): ").lower()

            if question in response_yes:
                random_num = random.randint(0, 101)
                play(random_num)
            else:
                print("Goodbye.")
                exit()


if __name__ == "__main__":
    play(random_num)
