# Understanding Turtle graphics and How to use the documentation.

from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()

screen.colormode(255)

# tim.shape("turtle")
# tim.color("coral")

# tim.forward(100)
# tim.right(90)

# tim.forward(100)
# tim.right(90)

# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# OR using for loop

# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 1

# colors = ["red", "coral", "plum", "blue", "green", "deep pink", "pale violet red", "goldenrod", "IndianRed", "CornflowerBlue", "DarkOrchid"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# Challenge 2 

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color


# directions = [0, 90, 180, 270]
# tim.pensize(15) 
# tim.speed("slow")


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Challenge 3

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()   #default value of tim.heading() is 0
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)


draw_spirograph(5)

screen.exitonclick()