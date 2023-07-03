import turtle as t
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# t.penup()
# t.write('Home = ', False, align="center", font=("Arial", 20, "normal"))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.title("snake game")
screen.tracer(0)


snake = Snake()

food = Food()

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.down, "Down",)
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True


while is_game_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    latest = snake.snake_segments[0].xcor()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.reload()
        snake.increase_position()
        snake.create_more_snake()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280:
        is_game_on = False
    if snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        is_game_on = False
    if snake.check_collision(latest):
        is_game_on = False


scoreboard.game_over()
    


screen.exitonclick()