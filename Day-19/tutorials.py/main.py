import turtle as t
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()


def move_forwards():
    new_turtle.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()