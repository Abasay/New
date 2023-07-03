import turtle as t
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=600)

is_race_on = False

user_bet = screen.textinput(title='make a guess', prompt='who will win the race among these colors? ["red", "orange", "yellow", "green", "blue", "purple"], make a guess: ')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_instances = []

def turtle_instance(turtlename, color, y):
    turtlename = Turtle("turtle")
    turtlename.penup()
    turtlename.color(color)
    turtlename.goto(x=-380, y=y)

    return turtlename

direction = -100

for i in range(0, 6):
    turtle_name = f"turtle{i}"
    my_turtle = turtle_instance(turtle_name, color=colors[i], y=direction)
    direction += 30
    turtle_instances.append(my_turtle)

screen.textinput(title='start the game', prompt="all is set, enter start to start the race")



if user_bet:
    is_race_on = True

while is_race_on:
    for new_turtle in turtle_instances:
        if new_turtle.xcor() > 380:
            win = new_turtle.color()[1]
            if user_bet == win:
                print(f"You win. {win} wins")
            else:
                print(f"You lose. {win} wins")
            
            is_race_on = False

        move_random = randint(0, 10)
        new_turtle.forward(move_random)

screen.exitonclick()