import random

play = "yes"
score = 0
round = 0

while play == "yes":
    round += 1
    user = input("Choose rock, paper, or scissors: ").lower()
    if user != "rock" and user != "paper" and user != "scissors":
        print("Invalid input. Please try again.")
        continue
    print("You chose: " + user)

    comp = random.randrange(1,3)
    if comp == 1:
        comp = "rock"
    elif comp == 2:
        comp = "paper"
    else:
        comp = "scissors"
    print("Computer chose: " + comp)

    if user == comp:
        print("It's a tie!")
    elif user == "rock" and comp == "scissors":
        print("You win!")
        score += 1
    elif user == "paper" and comp == "rock":
        print("You win!")
        score += 1
    elif user == "scissors" and comp == "paper": 
        print("You win!")
        score += 1
    else: 
        print("You lose!")

    play = input("Do you want to play again? (yes or no)").lower()

# print the number of rounds played and the score
print("You played " + str(round) + " rounds.")
print("Your score is: " + str(score))
print("Thanks for playing!")
