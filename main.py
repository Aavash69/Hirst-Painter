from colors import colors_list
import random
import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
screen.setup(height=500, width=500)

screen.colormode(255)

tim.up()
x = -225.0
y = -225.0

for _ in range(10):

    tim.setx(x)
    tim.sety(y)
    y += 50
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)

tim.hideturtle()

screen.exitonclick()
