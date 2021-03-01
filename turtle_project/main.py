import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)

timmy = turtle_module.Turtle()


colors = colorgram.extract('61RQCX9SJKL.jpg', 10)

colors_rgb = []
for color in colors:
    colors_rgb.append(color.rgb)

print(colors_rgb)


timmy.penup()

def move_straight():
    for _ in range(10):
        timmy.dot(20, random.choice(colors_rgb))
        timmy.forward(50)
        timmy.dot(20, random.choice(colors_rgb))


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

move_straight()

for _ in range(5):
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    move_straight()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    move_straight()
    timmy.dot(20, random.choice(colors_rgb))





screen = turtle_module.Screen()
screen.exitonclick()