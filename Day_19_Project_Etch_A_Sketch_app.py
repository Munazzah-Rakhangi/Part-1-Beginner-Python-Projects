# Higher order functions and Event Listeners
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(20)
    
def move_backward():
    timmy.backward(20)
    
def turn_left():
    # timmy.left(10)
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    # timmy.right(10)
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear)


screen.exitonclick()