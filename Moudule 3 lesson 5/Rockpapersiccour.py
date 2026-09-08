import random

while True:
    user_action = input("Enter a choice (rock, aper, scissors):")
    possible_actions = ["Rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose{user_action}, computer choes {computer_action}. \n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. it's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You Win!")

    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! You win.")
        else:
            print("Sissors cuts paper! You lose.")

    elif user_action == "scissors":
            if computer_action == "rock":
                print("scissors covers rock! You win.")
            else:
                print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n):")
    if play_again != "y":
        break
    
    
    
    
        