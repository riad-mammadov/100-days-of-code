from turtle import Screen
from snake import * 
import time
from food import *
from scoreboard import *
screen = Screen()

screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("grey")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        snake.extend()
        food.replace()
        score.increase()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        gameOn = False
        score.gameOver()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            gameOn = False
            score.gameOver() 
       
       






screen.exitonclick()