'''
print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is you age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Free ride for you")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wants_photo = input("Do you want to have a photo taken? Type y for yes and n for No.")
    if wants_photo == "y":
        #Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you cannot ride the rollercoster.")

'''

'''
print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ") 
add_pepperoni = input("Do you want pepperoni? Y or N ") 
extra_cheese = input("Do you want extra cheese? Y or N ") 

bill = 0

if size == "S":
  bill = 15
  print("Price for small pizza is $15")
elif size == "M":
  bill = 20
  print("Price for Medium pizza is $20")
else:
  bill = 25
  # print("Price for Large pizza is $25")

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

'''


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.\nYou're at a cross road.")
choice_1 = input('Where do you want to go?. \n Type "left" or "right" \n').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across').lower()
    if choice_2 == "wait":
        choice_3 = input("which door will you choose, Red, blue, yellow").lower()
        if choice_3 == "red":
            print("You got Burned by fire. Game Over.")
        elif choice_3 == 'blue':
            print("You got Eaten by beasts.Game Over")
        elif choice_3 == "Yellow":
            print("You win")
        else:
            print("door error. game over")
        
    else:
        print("You got attacked by an angry trout")
else:
    print("You have fallen into a hole. GAME OVER")
