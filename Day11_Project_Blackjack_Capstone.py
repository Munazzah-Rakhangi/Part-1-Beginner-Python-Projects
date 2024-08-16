# TODO-1: Create a deal_car() function that uses list to return a randam card.
import random
import Day11_Project_Blackjack_logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# TODO-3: Create a function called calculate_score() 
# that takes a List of cards as input and 
# returns the sum of all the cards in the List as the score. 

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # TODO-4: Inside calculate_score() 
    # check for blackjack (a hand with only 2 cards: Ace + 10) and 
    # return 0 instead of actual score. 0 will represent a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # TODO-5: Inside calculate_score() check of an 11(ace). 
    # If the score is already over 21, remove 11 and replace with 1. 
    # we can use append() and remove() functions
    if 11 in cards and sum (cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


# TODO-2: Deal the user and computer 2 cards each using deal_car() and append(). 

# TODO-10: Create a function called compare() 
# and pass in the user_score and computer_score.

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent ha Blackjack"
    elif u_score == 0:
        return "You win" 
    elif u_score > 21:
        return "You went over. You Lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else: 
        return "You Lose"

def play_game():
    print(Day11_Project_Blackjack_logo.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # TODO-6: Call the function calculate_score(). 
    # If the computer or the user has the blackjack(0) or if the users score is over 21, 
    # then the game ends.
    
    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # TODO-7: If the game has not ended, 
        # ask the user if they want to draw another card. 
        # If yes, then use deal_card() function to add another card to the user_cards list. 
        # If no, then game has ended
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
        # TODO-8 The sore will need to rechecked with every new card drawn
        # and the checks in the TODO-6 need to be repeated until the game ends.
        # Added while loop under Todo-6
        
        # TODO-9: Once the user is done, it's time to let the computer play.
        # The computer should keep drawing cards as long as it has the score less than 17.

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's Final cards: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 200)
    play_game()
    





     