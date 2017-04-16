#Imports the "random" library
import random

def game():
    # Generate a Random number between 1 - 1000
    secret_num = random.randint(1, 1000)

    # Keeps track of the number of guesses in an array
    guesses = []

    # Checks the length of "counter" to see if there are less than 20 guesses
    while len(guesses) < 20:

        # Get a number guess from the player
        try:
            guess = int(input("Guess a number between 1 and 1000: \n -->: "))
        except ValueError:
            print("That is not a number")
        else:
            # Compare the guess to the secret number
            if guess == secret_num:
                print(" -->: You got it!, the secret number was {}.".format(secret_num))
                break
            # Print hit/miss to show user how close they are
            elif guess < secret_num:        
                print(" -->: That's not it, the secret number is greater then what you've guessed.\n")
            elif guess > secret_num:        
                print(" -->: That's not it, the secret number is less then what you've guessed.\n")
            guesses.append(guess)

    else:
        print(" -->: You lost, the secret number was {}.".format(secret_num))

    play_again = input("Do you want to play again? Y/n ")

    if play_again.lower() != 'n':
        print ""
        print ""
        print ""
        game()
    else:
        print("Bye!")
        
game()
