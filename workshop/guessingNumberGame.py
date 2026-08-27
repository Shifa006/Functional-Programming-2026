import random

def guessingNumberGame():
    number = random.randint(0,10)
    while True:
        try:
            guess = int(input("Guess a number between 0-10 :"))
            if guess < 0 or guess > 10:
                raise ValueError
        except ValueError:
            print("Please enter a whole number between 0 and 10.")
            continue

        if guess == number:
            break
        print("try again")

    return "you guessed it right"

print(guessingNumberGame())

again = input("Do you want to play again? (yes/no): ")
while again == "yes":
    print(guessingNumberGame())
    again = input("Do you want to play again? (yes/no): ")
    if again == "no":
        print("Thank you for playing!")
        break
