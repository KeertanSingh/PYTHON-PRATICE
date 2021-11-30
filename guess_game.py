# guess number game
import random
def guessing():
    num = random.randint(1,10)
    i = 1
    total_moves = 6
    print("YOU HAVE TOTAL 5 MOVES TO PLAY GAME!!")
    while i <= 5:
        print("YOU HAVE =", total_moves - i)
        guess = int(input("GUESS NUMBER:"))

        # when you guessed right number
        if guess == num:
            print("YOU WON!!\nYOU TOOK", i, "MOVES TO GOT SUCCED")
            break

        # game over
        elif i >= 5:
                print("YOU LOOSE\nGAME OVER!")

        # when you will enter larger number
        elif guess > num:
            print("CHOOSE LESSER!!")

        # when you will enter lesser number
        elif guess < num:
            print("CHOOSE GREATER!!")

        else:
            continue
        i += 1

    # function to play the game again
    again()
def again():
    ask = input("DO YOU WANT TO PLAY AGAIN?\nyes or no\n")
    if ask == "yes":
        guessing()
    elif ask == "no":
        print("THANKS FOR PLAYING!!!")
    else:
        print("SOMETHING IS WRONG!!")
        again()
guessing()