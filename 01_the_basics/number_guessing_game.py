from random import randint


def win(computer, numbers):
    if computer == numbers:
        return True
    return False


def get_a_guess():
    return input("What is your guess? ")


def answer(computer, numbers, ):
    if computer == numbers:
        return "Wow...."

    elif computer > numbers:
        return "You guessed too Low"
    return "You guessed too high"


def welcome():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 20")
    print("Can you guess what number im thinking of?")


def finish(number, counter):
    print("Thank you for playing with me")
    print(f"The number was {number}")
    print(f"It took you {counter} tries to guess the number")
    answer = input("\nDo you want to play again? (Y/N)")
    if answer.upper() == "Y" or answer.upper() == "YES":
        return True
    else:
        return False


guess = -1
guess_counter = 0
continue_playing = True

welcome()

while continue_playing:
    computer_number = randint(1, 20)
    guess_counter = 0
    while not win(computer_number, guess):
        guess_counter += 1
        guess = int(get_a_guess())

        print(answer(computer_number, guess))

    continue_playing = finish(computer_number, guess_counter)
