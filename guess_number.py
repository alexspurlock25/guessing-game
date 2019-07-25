# Alex (Sasha) Spurlock
# alexanderspurlock@gmail.com

import random

random_number = random.randint(0,101)
print(f"New number random is {random_number}") ## for testing

guess_list = []
all_guesses = []

user_number = int( input("Guess a number between 0 and 100: ") )
guess_list.append(user_number)
all_guesses.append(user_number)


def wrong_number(user_number):

    '''

    This method has a while loop that makes the user keep guessing.
    When the user finally guesses right, the loop becomes false,
    then the number is sent to 'right_number' method to determine the user's next course of action.

    This method is 'skipped' if the user guesses right on his/her first try.

    '''

    while random_number != user_number:

        if user_number < 0 or user_number > 100:

            if user_number < 0:
                user_number = int( input(f"{user_number} is below specified range. Try again: ") )
                guess_list.append(user_number)
                all_guesses.append(user_number)

            else:
                user_number = int( input(f"{user_number} is above specified range. Try again: ") )
                guess_list.append(user_number)
                all_guesses.append(user_number)

        elif abs(user_number - random_number) > 0 and abs(user_number - random_number) <= 5:

            user_number = int( input(f"{user_number} IS BURNING: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

        elif abs(user_number - random_number) > 5 and abs(user_number - random_number) <= 10:

            user_number = int( input(f"{user_number} is HOT: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

        elif abs(user_number - random_number) > 10 and abs(user_number - random_number) <= 20:

            user_number = int( input(f"{user_number} is REALLY WARM: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

        elif abs(user_number - random_number) > 20 and abs(user_number - random_number) <= 30:

            user_number = int( input(f"{user_number} is WARMER: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

        elif user_number > random_number:

            user_number = int( input(f"{user_number} is too high. Try Again: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

        elif user_number < random_number:

            user_number = int( input(f"{user_number} is too low. Try Again: ") )
            guess_list.append(user_number)
            all_guesses.append(user_number)

    return right_number(user_number)

def right_number(right_user_number):

    '''

    This method is for situations in which the user's numbers are correct.
    Whether it's his/her first guess or after guessing several times.

    '''

    print(f"{right_user_number} is right! Good Job!")

    question = input("Would you like to play again? ").lower()

    if question == 'yes' or question == 'yeah':
        guess_list.clear()

        new_random_number = random.randint(0, 101)
        print(f"New random number is {new_random_number}") # this line is only for testing

        new_user_number = int( input("Okay, let's play again. Enter a number between 0 and 100: ") )
        guess_list.append(new_user_number)
        all_guesses.append(new_user_number)

        if new_user_number == new_random_number and len(guess_list) == 1:

            return first_time_guess(new_user_number)

        else:
            return wrong_number(new_user_number)

    else:
        return print("Have a good day! These are your results!\n")


def first_time_guess(first_try_number):

    question = input("WOW!! You guessed on your first try! NICE! Would you like to play again? ").lower()

    if question == "yes" or question == "yeah":
        guess_list.clear()

        new_random_number = random.randint(0,101)
        print(f"New random number is {new_random_number}")  # for testing

        new_user_number = int( input("Okay, let's see if you can get it on your first try again!!\n"
                                     "Enter a number here: ") )
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
