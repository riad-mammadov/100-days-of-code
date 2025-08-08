from turtle import Screen, Turtle

t = Turtle()


for i in range(4, 11):
    angle = 360 / i
    for _ in range(i):
        t.forward(70)
        t.right(angle)


screen = Screen()
screen.exitonclick()