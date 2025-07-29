import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
