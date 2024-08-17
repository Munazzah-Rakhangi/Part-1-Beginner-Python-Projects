import random
from Day13_Project_Higher_lower_data import data
from Day13_Project_Higher_lower_logo import logo, vs

def format_data(account):
    """Takes the account data and returns data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take user's guess and there follower count and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
        

# Display art
print(logo)

# Storing the score
score = 0

#Repeating the game using while loop
game_continue = True

account_b = random.choice(data)

while game_continue:
    # Generate a random account from game data
    
    # Making account at position B become the next acount at position A.
    account_a = account_b
    account_b = random.choice(data)
    
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess. 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear the screen
    print("\n" * 20)
    print(logo)

    ## Get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_a["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Check if user is correct
    ## Use if statement to check if the user is correct.

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're Right! Current score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score is {score}")
        game_continue = False


