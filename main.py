from game_data import data
from art import logo, vs
import random

def account_info(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_cty = account["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_cty}"

def check_option(user_choice, follower_a, follower_b):
    if follower_a > follower_b:
        return user_choice == "a"
    else:
        return user_choice == "b"

def higher_lower_game():
    print(logo)
    score = 0
    option_b = random.choice(data)
    game_on = True

    while game_on:
        option_a = option_b
        # Ensure option_b is different from option_a
        while True:
            option_b = random.choice(data)
            if option_a != option_b:
                break

        print(f"Compare A: {account_info(option_a)}.")
        print(vs)
        print(f"Against B: {account_info(option_b)}.")

        # Get user input and validate it
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_choice not in ["a", "b"]:
            user_choice = input("Invalid choice. Please type 'A' or 'B': ").lower()

        print("\n" * 20)  # Clear screen
        print(logo)

        follower_a = option_a["follower_count"]
        follower_b = option_b["follower_count"]
        is_user_correct = check_option(user_choice, follower_a, follower_b)

        if is_user_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            play_again = input("Do you want to play again? Type 'yes' to play again or 'no' to stop: ").lower()
            if play_again == "yes":
                print("Thank you! Starting a new game...")
                score = 0
                option_b = random.choice(data)
            else:
                print("Thanks for playing! Come back soon.")
                game_on = False

# Start the game
higher_lower_game()
