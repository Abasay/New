import turtle as t
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()



def move_forwards():
    """function to move forwards"""
    new_turtle.forward(20)

def move_backwards():
    """function to move backwards"""
    new_turtle.backward(20)

def counter_clockwise():
    """function to change the heading to counter-clocwise"""
    new_heading = new_turtle.heading() + 18
    new_turtle.setheading(new_heading)

def clockwise():
    """function to change the direction to clockwise"""
    new_heading = new_turtle.heading() - 18
    new_turtle.setheading(new_heading)

def reset():
    """function to clear the drawings and reset the turtle positions"""
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()

    
    # new_turtle.reset()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=reset)


screen.exitonclick()