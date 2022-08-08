# Guess the number
# no. of guess
try:
    secretNumber = 18  # Creating the secret number
    totalMoves = 5  # number of moves
    takenMove = 0  # Count move
    print(f"""Welcome To Guess Number Game.
# You have just {totalMoves} moves.
# Follow the hint.""")  # Introduction before game

    while True:
        guess_number = int(input("\nGuess the number: "))
        totalMoves -= 1

        if totalMoves == 0 and guess_number != secretNumber:
            """ if move will be zero then it will execute"""
            print("You loose the game!")
            break

        if guess_number == secretNumber:
            """when you we guess the right number."""
            takenMove += 1
            print(f"You have took {takenMove} moves!!")
            print("You won!")
            break

        elif guess_number < secretNumber:
            """ When you will input small number than secret number"""
            print("Hint: Choose greater number!!")
            takenMove += 1

        elif guess_number > secretNumber:
            """ When You will input greater number than secret number."""
            print("Hint: Choose smaller number!!")
            takenMove += 1

        print(f"Moves left: {totalMoves}")
        # printing the number of moves.
except:
    print("Please, give input as intergers.")
