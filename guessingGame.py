import random

actual = random.randrange(1, 9)

chances=0

print("Welcome to the Python Number Guessing Game!")
print("You have 5 chances to guess the correct number")
print("Best of Luck!")

while chances < 5:
    guess = int(input("Enter a numerical value: "))
    chances = chances + 1

    if guess < actual:
        print("That's too low! Try a number higher than ", guess)
        
    if guess > actual:
        print("That's too high! Try a number lower than ", guess)

    if guess == actual:
        print("You win! How do you feel?")
        break

    if not chances < 5:
        print("You lose! The number actualy was ", actual, ". Do better next time!")
        



