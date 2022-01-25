from random import randint

moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or end the game)").lower()
    if player == "end the game":
        print("the ganme has ended")
        break
    elif player == computer:
        print("tie")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    elif player == "paper":
        if computer == "rock":
            print("You Lose", computer, "beats", player)
        else:
            print("you win", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You win", player, "beats", computer)
    else:
            print("Check your spelling")
