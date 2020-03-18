# Alex (Sasha) Spurlock
# alexanderspurlock@gmail.com

import random

# variable to hold random number. 0 to 100
random_number = random.randint(0, 101)
print(f"New random number is {random_number}")  ## for testing

guess_list = []
all_guesses = []

isValidInput = False
user_number = 0
while not isValidInput:
    try:
        #The number we are trying to guess
        user_number = int(input("Guess a number between 0 and 100: "))
        isValidInput = True
    except ValueError: 
        print("{} is not a valid number.  Please enter another guess".format(user_number))


guess_list.append(user_number)
all_guesses.append(user_number)


def wrong_number(num):
    """

    This method has a while loop that makes the user keep guessing.
    When the user finally guesses right, the loop becomes false,
    then the number is sent to 'right_number' method to determine the user's next course of action.

    This method is 'skipped' if the user guesses right on his/her first try.

    """

    while random_number != num:

        if num < 0 or num > 100:

            if num < 0:
                num = int(input(f"{num} is below specified range. Try again: "))
                guess_list.append(num)
                all_guesses.append(num)

            else:
                num = int(input(f"{num} is above specified range. Try again: "))
                guess_list.append(num)
                all_guesses.append(num)

        elif abs(num - random_number) > 0 and abs(num - random_number) <= 5:

            num = int(input(f"{num} IS BURNING: "))
            guess_list.append(num)
            all_guesses.append(num)

        elif abs(num - random_number) > 5 and abs(num - random_number) <= 10:

            num = int(input(f"{num} is HOT: "))
            guess_list.append(num)
            all_guesses.append(num)

        elif abs(num - random_number) > 10 and abs(num - random_number) <= 20:

            num = int(input(f"{num} is REALLY WARM: "))
            guess_list.append(num)
            all_guesses.append(num)

        elif abs(num - random_number) > 20 and abs(num - random_number) <= 30:

            num = int(input(f"{num} is WARMER: "))
            guess_list.append(num)
            all_guesses.append(num)

        elif num > random_number:

            num = int(input(f"{num} is too high. Try Again: "))
            guess_list.append(num)
            all_guesses.append(num)

        elif num < random_number:

            num = int(input(f"{num} is too low. Try Again: "))
            guess_list.append(num)
            all_guesses.append(num)

    return right_number(num)


def right_number(num):
    """

    This method is for situations in which the user's numbers are correct.
    Whether it's his/her first guess or after guessing several times.

    """

    print(f"{num} is right! Good Job!")

    question = input("Would you like to play again? ").lower()
    
    if question in ["y","yes","yeah","yep"]:
        guess_list.clear()

        new_random_number = random.randint(0, 101)
        print(f"New random number is {new_random_number}")  # this line is only for testing

        new_user_number = int(input("Okay, let's play again. Enter a number between 0 and 100: "))
        guess_list.append(new_user_number)
        all_guesses.append(new_user_number)

        if new_user_number == new_random_number and len(guess_list) == 1:

            return first_time_guess(new_user_number)

        else:
            return wrong_number(new_user_number)

    else:
        return print("Have a good day! These are your results!\n")


def first_time_guess(num):
    question = input("WOW!! You guessed on your first try! NICE! Would you like to play again? ").lower()

    if question in ["y","yes","yeah","yep"]:
        guess_list.clear()

        new_random_number = random.randint(0, 101)
        print(f"New random number is {new_random_number}")  # for testing

        new_user_number = int(input("Okay, let's see if you can get it on your first try again!!\n"
                                    "Enter a number here: "))
        guess_list.append(new_user_number)
        all_guesses.append(new_user_number)

        if new_user_number == new_random_number and len(guess_list) == 1:

            return first_time_guess(new_user_number)

        else:
            return wrong_number(new_user_number)

    else:
        return print("Have a wonderful day! These are your results!\n")


if user_number == random_number and len(guess_list) == 1:

    first_time_guess(user_number)

elif user_number == random_number:

    right_number(user_number)

else:

    wrong_number(user_number)

print(f"Last session guesses: {guess_list}")
print(f"All your guesses from all your games: {all_guesses}")
