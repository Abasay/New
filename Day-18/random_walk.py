import turtle as t
from turtle import Turtle, Screen
from random import choice, randint


t.colormode(255)

instance = Turtle()

instance.pensize(10)
instance.speed(8)


def random_colors():
    """function to generate random rgb colors"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb
def east():
    instance.forward(40)

def north():
    instance.left(90)
    instance.forward(40)

def west():
    instance.backward(40)

def south():
    instance.right(90)
    instance.forward(40)

walks = [north, south, east, west]

for walk in range(500):
    instance.pencolor(random_colors())
    choice(walks)()
    


tim = Turtle()
directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(choice(directions))






screen = Screen()
screen.bgcolor('red')
screen.exitonclick()
