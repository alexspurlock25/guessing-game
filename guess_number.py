# Alex (Sasha) Spurlock
# alexanderspurlock@gmail.com

import random

random_number = random.randint(0,101)
print(random_number)

guess_list = []

user_number = int( input("Guess a number between 0 and 100: ") )
guess_list.append(user_number)

def wrong_number(user_number):

    while random_number != user_number:

        if user_number < 0 or user_number > 100:

            if user_number < 0:
                user_number = int( input(f"{user_number} is below specified range. Try again: ") )
                guess_list.append(user_number)

            else:
                user_number = int( input(f"{user_number} is above specified range. Try again: ") )
                guess_list.append(user_number)

        elif abs(user_number - random_number) <= 10:

            user_number = int( input(f"{user_number}is HOT: ") )
            guess_list.append(user_number)

        elif abs(user_number - random_number) > 10 and abs(user_number - random_number) <= 20:

            user_number = int( input(f"{user_number} is WARM: ") )
            guess_list.append(user_number)

        elif abs(user_number - random_number) > 20 and abs(user_number - random_number) <= 30:

            user_number = int( input(f"{user_number} is WARMER: ") )
            guess_list.append(user_number)

        elif user_number > random_number:

            user_number = int( input(f"{user_number} is too high. Try Again: ") )
            guess_list.append(user_number)

        elif user_number < random_number:

            user_number = int( input(f"{user_number} is too low. Try Again: ") )
            guess_list.append(user_number)

    return right_number(user_number)

def right_number(user_number):

        print(f"{user_number} is right! Good Job!")
        guess_list.append(user_number)

        question = input("Would you like to play again? ").lower()

        if question == 'yes' or question == 'yeah':

            user_number = int( input("Okay, let's play again. Enter a number between 0 and 100: ") )
            guess_list.append(user_number)

            if user_number == random_number:
                return right_number(user_number)

            else:
                return wrong_number(user_number)

if user_number == random_number:

    right_number(user_number)

else:

    wrong_number(user_number)

print(f"Have a good day! Your guesses are {guess_list}")
