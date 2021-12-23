# Alexander Spurlock

import random

def play(rand_num:int):
    try:
        user_num = int(input("Guess a number between 0 and 100: "))
        check_guess(user_num, rand_num)

    except ValueError:
        print("NOT VALID INPUT.")
        play(rand_num)


def check_guess(guess, rand_num):
    while guess != rand_num:
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
            response_yes = ["y", "yes", "yeah", "yep"]
            print("You guessed the right number.")
            question = input("Would you like to play again? (y, yes, yeah, yep): ").lower()

            if question in response_yes:
                play(random.randint(0, 101))
            else:
                print("Goodbye.")
                exit()


if __name__ == "__main__":
    random_num = random.randint(0, 101)
    print(f"(FOR TESTING. COMMENT THIS OUT.) New random number is {random_num}")  # for testing
    
    play(random_num)
