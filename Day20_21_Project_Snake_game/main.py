from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

# By default our turtle demension is 20x20 (widthxheight)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
# Step 2: Animating the snake segments
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    # Detect collison with food
    if snake.head.distance(food) < 15:   #distance method helps us to detect the distance from one turtle (snake) to another turtle(food)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect collison with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    
    # detect collision with tail
    
    # CODE WITHOUT SLICING
    # for segment in snake.segments:
        # if segment == snake.head:       #head is the first segment so if segment is snakes head then continue
    #         pass
    #     elif snake.head.distance(segment) < 10:   #head is the first segment
    #         game_is_on = False
    #         scoreboard.game_over()
    
    # CODE WITH SLICING
    for segment in snake.segments[1:]:     # 1: means except the 1st segment because first segment is head
        if snake.head.distance(segment) < 10:   #head is the first segment
            game_is_on = False
            scoreboard.game_over()
    

 

 





screen.exitonclick()