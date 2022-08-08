# Snake, water, game
import random

game_item = ["s", "w", "g"]
i = 1
moves = 5
print(f"""Welcome to Snake, Water And Gun
Press 's' for snake
Press 'w' for water
press 'g' for gun
Total Moves: {moves}""")
computer_score = 0
your_score = 0
while True:
    if i > moves:
        break

    computer_choice = random.choice(game_item)
    choice = input("\nEnter your choice: ").lower()
    # print(i)

    if choice == computer_choice:
        print(f"Computer choice: {computer_choice}")

        print("Both choice Same")

    # you win
    elif choice == "s" and computer_choice == "w":
        print(f"Computer choice: {computer_choice}")
        print("you win!")
        your_score += 1

    elif choice == "w" and computer_choice == "g":
        print(f"Computer choice: {computer_choice}")
        print("you win!")
        your_score += 1

    elif choice == "g" and computer_choice == "s":
        print(f"Computer choice: {computer_choice}")
        print("you win!")
        your_score += 1

    # computer win
    elif computer_choice == "s" and choice == "w":
        print(f"Computer choice: {computer_choice}")
        print("Computer win!")
        computer_score += 1

    elif computer_choice == "w" and choice == "g":
        print(f"Computer choice: {computer_choice}")
        print("Computer win!")
        computer_score += 1

    elif computer_choice == "g" and choice == "s":
        print(f"Computer choice: {computer_choice}")
        print("Computer win!")
        computer_score += 1

    else:
        print("Invalid input")

    print(f"Moves left:{moves - i}")

    i += 1


def result(player1, player2):
    print("\n*****Result*****")
    if player1 > player2:
        print(f"Your score : {your_score}")
        print(f"Computer_score : {computer_score}")
        print("Computer is winner!")
    elif player1 < player2:
        print(f"Your score : {your_score}")
        print(f"Computer_score : {computer_score}")
        print("You are winner!!")
    else:
        print(f"Your score : {your_score}")
        print(f"Computer_score : {computer_score}")
        print("Match tie")


result(computer_score, your_score)
