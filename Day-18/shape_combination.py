from turtle import Turtle, Screen
from random import choice

_shape = Turtle()
# _shape.pensize(10)

colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_function(sides):
    """function to draw the different dhspes"""
    degree = float((sides - 2) * 180)
    angle = float(180 - (degree / sides))
    for _ in range(sides):
        _shape.forward(100)
        _shape.right(angle)


for side in range(3, 11):
    _shape.pencolor(choice(colors))
    draw_function(side)

def square():
    """functiion to draw a square"""
    _shape.pencolor('red')
    for i in range(4):
       _shape.forward(100)
       _shape.right(90)
    return


def triangle():
    """function to draw a triangle"""
    _shape.pencolor('green')
    for _ in range(3):
        _shape.forward(100)
        _shape.right(120)
    return

def pentagon():
    """function to draw a pentagon"""
    _shape.pencolor('blue')
    for _ in range(5):
        _shape.forward(100)
        _shape.right(72)
    return


def hexagon():
    """function to draw hexagon"""
    _shape.pencolor('yellow')
    for _ in range(6):
        _shape.forward(100)
        _shape.right(60)
    return

def heptagon():
    """function to draw heptagon"""
    _shape.pencolor('brown')
    for _ in range(7):
       _shape.forward(100)
       _shape.right(51.428)


def octagon():
    """function to draw an octagon"""
    _shape.pencolor('coral')
    for _ in range(8):
        _shape.forward(100)
        _shape.right(45)
    return
def nonagon():
    """function to draw a nonagon"""
    _shape.pencolor('violet')
    for _ in range(9):
        _shape.forward(100)
        _shape.right(40)
    return

def decagon():
    """function to draw a decagon"""
    _shape.pencolor('orange')
    for _ in range(10):
        _shape.forward(100)
        _shape.right(36)
    return

def shape():
    square()
    triangle()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nonagon()
    decagon()

    return
# shape()

screen = Screen()
screen.exitonclick()
