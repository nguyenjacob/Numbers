import random

guesses = 0

print("Get Guessing!")

number = random.randint(1, 30)
while guesses < 5:
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess > number:
        print("Nope, too high!")

    if guess < number:
        print("Nope, too low!")

    if guess == number:
        print("Good Job"". You got the number in", guesses, "guesses!")

if guess != number:
    print("Sorry," "I was thinking of", number,)