from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

myScreen = Screen()

print(myScreen.canvheight)

myScreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "squirtle", "Charmander"])
table.add_column("Pokemon Type",["Electric", "Water", "Fire"])
table.align = "l"

print(table)