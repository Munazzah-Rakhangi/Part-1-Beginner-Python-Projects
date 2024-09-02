from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x= new_x, y= new_y)
        
    def bounce_y(self):
        self.y_move *= -1     # reversing the y_move in y direction because when the ball bounces we want it to come in opposite y direction.
        
    def bounce_x(self):
        self.x_move *= -1      # reversing the x_move in x direction because when the ball bounces the paddle we want it to come in opposite x direction.
        self.move_speed * 0.9
        
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()