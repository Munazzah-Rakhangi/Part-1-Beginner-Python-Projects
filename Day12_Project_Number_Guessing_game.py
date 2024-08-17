# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength)  #This gives error because we are trying to acess it beyond the scope


# Global scope
# player_heath = 10  #As this is not inside another function so it has global scope

# def drink_potion():
#     potion_strength = 2  #THIS IS LOCAL VARIABLE
#     print(player_heath)
    
# drink_potion()


# How to modify Global Variable
enemies = 0

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# Pyhton constants and global scope
# Global constants  // These are values which we do not want to change ever again.

# Global constants
# PI = 3.14159
# GOOGLE_URL = "https://www.google.com"

# def my_func():
#     print(GOOGLE_URL)


# -----------------------------------------------------------------------------------------------------------------
# NUMBER GUESSING GAME
# =================================================================================================================
from random import randint
from Day12_Project_Number_Guess_logo import logo

# Global constants down here
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



# A function to check a users guess against actual number
def check_answer(user_guess, actual_answer, turns):
    '''Checks answer agaiants guess, returns the number of turns remaining'''
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1 
    elif user_guess< actual_answer:
        print("Too Low.")
        return turns - 1 
    else:
        print(f"You got it! The answer was {actual_answer}")
        
# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
    if level == "easy":
    # Not using this way because we want to call the def set_difficulty function down
    #     turns = EASY_LEVEL_TURNS
    # else:
    #     turns = HARD_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 to 100
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100!")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")


    turns = set_difficulty()
    
    
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")

    # Track the number of turns and reduce by 1 if they get it wrong
    
game()