program_dictionary = {
    "Bug" : "An error in code",
    "Function": "A piece of code",
}

# print(program_dictionary["Bug"])

program_dictionary["Loop"] = "Repeating actions"

# print(program_dictionary)

# empty_dictionary = {}

# wipe an exting dictionary

# program_dictionary = {}

# # Edit an item in a dictionary
# program_dictionary["Bug"] = "A moth in your computer"
# print(program_dictionary)

# Loop through a dictionary

# for key in program_dictionary:
#     print(key)
#     print(program_dictionary[key])


# # Grading Program 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     # print(scores)
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
        
# print(student_grades)


# Nesting Lists and Dictionaries

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin" ,
}

# Nested List in dictionary

# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


# travel_log = {
#     "France" : {
#         "cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12
#     },
    
#     "Germany" : {
#         "cities_visited" : ["Stuttgart", "Berlin", "Hamburg"],
#         "total_visits" : 15
#     }
# }

# print(travel_log["Germany"]["cities_visited"][2])

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2])


# ******************************************************************************************************
# *******************************************************************************************************

# THE SECRET AUCTION PROGRAM 

import Day9_Project_The_secret_auction_logo
print(Day9_Project_The_secret_auction_logo.logo)

# TODO-1: Ask the user for input
# name = input("what is your name?: ")
# price = int(input("Enter your bid price: $"))

# TODO-2: Save the data into a dictionary {name:price}
# bids[name] = price  #stores the name and price as the key value pairs

# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with the bid of ${highest_bid}.")


# TODO-3: Whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'yes or 'no'\n")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("Enter your bid price: $"))
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type 'yes or 'no'\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 200)
    
