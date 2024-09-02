from turtle  import Turtle
import random

# Using class inheritance
# Inheriting from Turtle class

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # The height and width of our screen is 600hx600w
        # X axis goes from -300 to 300 Y axis goes from 300 to -300
        # We don't want our food at the edge of our screen so subtracting little bit we get 
        # for X axis -280 to 280 and Y axis 280 to -280
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)