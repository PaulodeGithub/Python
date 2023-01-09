import turtle

import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("image2.jpeg", 30)
#
#
# rgb_colors = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
turtle.colormode(255)
colors_list = [
            (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62),
            (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67),
            (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11),
            (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227), (59, 16, 31)
             ]

t = Turtle()
t.color("green")
t.shape("turtle")
t.pensize(6)
t.setheading(225)
t.penup()
t.hideturtle()
t.forward(340)
t.setheading(0)


number_dots = 101

random_col = random.choice(colors_list)
for dot_count in range(1, number_dots):
    t.dot(10, random.choice(colors_list))
    t.penup()
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.penup()
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen = Screen()
screen.exitonclick()





