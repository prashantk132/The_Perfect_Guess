import random
randNumber = random.randint(1,5)      # Imports random number between 1 to 5 including 1 and 5
guesses = 0
userGuess = None

while userGuess != randNumber:
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if userGuess == randNumber:
        print("You Guessed it Right!")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    
print(f"You guessed the number in {guesses} guesses")
with open ("hiscore.txt", "w") as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("You have just broken the high score")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))