# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('Day18_Project_Hirst_Painting/image.jpeg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fast")
tim.penup()
tim.hideturtle()
color_list = [(233, 233, 232), (231, 233, 237), (235, 232, 233), (224, 232, 226), (207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 206, 107), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 69), (186, 94, 106), (185, 140, 172), (85, 120, 180), (59, 39, 31), (87, 157, 91), (78, 153, 164), (195, 79, 72), (161, 201, 219), (80, 74, 44), (45, 74, 77), (57, 128, 125), (218, 176, 187), (220, 181, 168), (169, 207, 169)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()


