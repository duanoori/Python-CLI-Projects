import random
comp = random.randint(1,100)
print("Welcome To The Number Guessing Game In Python!")
print("I have selected a number from 1-100. Can you guess it?")
play = "yes"
while play.lower() == "yes":
    guess =int(input("Enter Your Guess: "))

    if guess > comp: 
        print("It's Too High")
    elif guess < comp:
        print("It's Too Low")
    else:
        print("You Guessed It Right!")
        print("Thanks For Playing!")    
        print("The Number Was: ", comp)
        play = input("Do You Want To Play Again? (yes or no): ")
