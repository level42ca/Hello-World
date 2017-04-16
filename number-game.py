#Imports the "random" library
import random

def game():
    # Generate a Random number between 1 - 10
    secret_num = random.randint(1, 10)
    
    # Keeps track of the number of guess'
    counter = []
    
    while len(counter) < 5:
    
        # Get a number guess from the player
        try:
            guess = int(input("Guess a number between 1 and 10: \n -->: "))
        except ValueError:
            print("That is not a number")
        else:
            # Compare the guess to the secret number
            if guess == secret_num:
                print("You got it!, the secret number was {}.".format(secret_num))
                break
            elif guess < secret_num:        
                print("That's not it, the secret number is greater then what you've guessed.\n")
            elif guess > secret_num:        
                print("That's not it, the secret number is less then what you've guessed.\n")
            counter.append(guess)
                
                
            # print hit/miss
    else:
        print("You lost, the secret number was {}.".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")
game()