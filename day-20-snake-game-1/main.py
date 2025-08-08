from turtle import Screen
from snake import * 
import time
screen = Screen()

screen.setup(400,400)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

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






screen.exitonclick()