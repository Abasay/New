from turtle import Turtle, Screen
from random import randint
import turtle as t

t.colormode(255)
circle = Turtle()
circle.speed("fastest")

def random_colors():
    """function to generate random rgb colors"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb

def spirograph(size):
    for _ in range(int(360 / size)):
       circle.pencolor(random_colors())
       circle.circle(100)
       # circle.setheading(circle.heading() + 10 )
       circle.left(size)

spirograph(5)


























screen = Screen()
# screen.bgcolor('red')
screen.exitonclick()
