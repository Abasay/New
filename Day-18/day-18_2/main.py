import colorgram
import turtle as t
from turtle import Turtle, Screen
from random import choice

rgbInstances = colorgram.extract('hirst.jpg', 30)
rgbList = []

t.colormode(255)
hirst = Turtle()

# for color in rgbInstances:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgbList.append((r, g, b))

colors = [(240, 238, 235), (225, 229, 234), (235, 230, 234), (234, 238, 236), (136, 169, 200), (191, 162, 140), (64, 89, 135), (183, 153, 171), (119, 77, 99), (153, 75, 50), (55, 118, 94), (220, 228, 87), 
(113, 115, 181), (45, 52, 105), (37, 44, 59), (129, 194, 143), (177, 187, 212), (225, 134, 16), (176, 94, 112), (81, 49, 66), (58, 46, 57), (110, 39, 37), (108, 166, 73), (215, 179, 193), (40, 49, 45), (46, 38, 35), (221, 83, 45), (231, 176, 158), (23, 95, 80), (148, 206, 214)]
hirst.speed("fastest")

def horizontal(size, spacing, radius):
    """function to print the horizontals"""
    for _ in range(size):
        color = choice(colors)
        hirst.dot(radius, color)
        hirst.penup()
        hirst.forward(spacing)
        hirst.pendown()

height = -200
def vertical(height):
    """function to change the position"""
    hirst.penup()
    hirst.sety(height)
    hirst.setx(-200)
    hirst.pendown()


for _ in range(10):
    vertical(height)
    height += 50
    horizontal(10, 50, 20)
hirst.hideturtle()

screen = Screen()
screen.exitonclick()