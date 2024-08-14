import random

#Random Heads and Tails Generator
'''
random_integer = random.randint(0,1)
# print(random_integer)

if random_integer == 0:
    print("Heads")
else:
    print("Tails")
    
'''

#Bankers Roulette - Who will pay the bill ?
'''
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# Option2
random_index = random.randint(0,4)
print(friends[random_index])
'''


#Rock paper and Scissors Game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Loose!")
elif computer_choice > user_choice:
    print("You Loose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
