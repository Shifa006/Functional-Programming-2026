import random

def guessingNumberGame():
    number = random.randint(0,10)
    guess = int(input("Guess a number between 0-10 :"))
    while guess != number :
        print("try again")
        guess = int(input("Guess a number between 0-10 :"))
    return "you guessed it right"

print(guessingNumberGame())

again = input("Do you want to play again? (yes/no): ")
while again == "yes":
    print(guessingNumberGame())
    again = input("Do you want to play again? (yes/no): ")
    if again == "no":
        print("Thank you for playing!")
        break
