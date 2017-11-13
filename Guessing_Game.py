import random

rounds = 0
numbers = 0
players = input("Welcome to Guessing Game. Choose a difficulty. 1. Easy(10) 2.Medium(15) 3.Hard(30)")

def easy():
    global rounds
    global numbers
    print("Player 1 start.")
    num = random.randrange(1, 10)



    while True:
        guess = int(raw_input("Guess a number."))

        if guess < num:
            print("Higher")
            rounds = rounds + 1
        elif guess > num:
            print("Lower")
            rounds = rounds + 1
        else:
            rounds = rounds + 1
            print("You got it right. " +  str(rounds))
            break
    print("Player 2 start.")
    num = random.randrange(1, 10)

    while True:
        guess = int(raw_input("Guess a number."))
        if guess < num:
            print("Higher")
            numbers = numbers + 1
        elif guess > num:
            print("Lower")
            numbers = numbers + 1
        else:
            numbers = numbers + 1
            print("You got it right. " + str(numbers))
            break
    if numbers >= 10 and rounds >= 10:
        print("Both players lose.")

    elif rounds >= 10:
        print("Player 1 you lose")

    elif numbers >= 10:
        print("Player 2 you lose")

    else:
        restart = easy()
        restart

def medium():
    global rounds
    global numbers
    print("Player 1 start.")
    num = random.randrange(1, 20)

    while True:
        guess = int(raw_input("Guess a number."))

        if guess < num:
            print("Higher")
            rounds = rounds + 1
        elif guess > num:
            print("Lower")
            rounds = rounds + 1
        else:
            rounds = rounds + 1
            print("You got it right. " + str(rounds))
            break
    print("Player 2 start.")
    num = random.randrange(1, 20)

    while True:
        guess = int(raw_input("Guess a number."))
        if guess < num:
            print("Higher")
            numbers = numbers + 1
        elif guess > num:
            print("Lower")
            numbers = numbers + 1
        else:
            numbers = numbers + 1
            print("You got it right. " + str(numbers))
            break
    if numbers >= 15 and rounds >= 15:
        print("Both players lose")
    elif rounds >= 15:
        print("Player 1 you lose")
    elif numbers >= 15:
        print("Player 2 you lose")
    else:
        restart = medium()
        restart


def hard():
    global rounds
    global numbers
    print("Player 1 start.")
    num = random.randrange(1, 100)



    while True:
        guess = int(raw_input("Guess a number."))

        if guess < num:
            print("Higher")
            rounds = rounds + 1
        elif guess > num:
            print("Lower")
            rounds = rounds + 1
        else:
            rounds = rounds + 1
            print("You got it right. " +  str(rounds))
            break
    print("Player 2 start.")
    num = random.randrange(1, 100)

    while True:
        guess = int(raw_input("Guess a number."))
        if guess < num:
            print("Higher")
            numbers = numbers + 1
        elif guess > num:
            print("Lower")
            numbers = numbers + 1
        else:
            numbers = numbers + 1
            print("You got it right. " + str(numbers))
            break
    if numbers >= 30 and rounds >= 30:
        print("Both players lose")
    elif rounds >= 30:
        print("Player 1 you lose")
    elif numbers >= 30:
        print("Player 2 you lose")
    else:
        restart = hard()
        restart


if players == 1:
    easy()
elif players == 2:
    medium()
else:
    hard()
