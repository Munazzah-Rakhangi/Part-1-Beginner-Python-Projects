# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# myScreen = Screen()

# print(myScreen.canvheight)

# myScreen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu", "squirtle", "Charmander"])
# table.add_column("Pokemon Type",["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)

# ===================================================================================

# How to create your own class in python

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(user_id="001", username="angela")
user_2 = User(user_id="002", username="Yu")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)




 