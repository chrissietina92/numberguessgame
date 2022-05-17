import random

# a number game where we think of a number between 1 and 100
# and the computer has to try and guess it.


def guessthenumber():

    compGuess = random.randint(1, 99)
    print("Pick a number between 0 and 100, not inclusive, and the computer will try and guess what it is")
    print("The computers guesses ", compGuess)

    y = input("Is this your number Y/N? ")
    l = 1
    h = 99

    while y != "Y":
        z = input("Is the computers guess > or < than your number? ")
        if z == "<":
            l = compGuess + 1
            newGuess = random.randint(l, h)
            print("The next guess is ", newGuess)
        else:
            h = compGuess - 1
            newGuess = random.randint(l, h)
            print("The next guess is ", newGuess)

        y = input("Is this your number Y/N? ")
        compGuess = newGuess
    print("The computer guessed your number!")



guessthenumber()
        
    
