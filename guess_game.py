import random

def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")

    #Generate a random number
    secret_number  = random.randint(1,100)

    attempts = 0
    guess = None

    #keep asking until user guesses right
    while guess != secret_number:
        try:
            guess = int(input("Enter a number: "))
            attempts +=1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else: 
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number.")

#run the game
number_guess_game()
