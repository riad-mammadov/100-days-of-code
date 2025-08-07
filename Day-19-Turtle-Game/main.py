from turtle import Screen, Turtle

t = Turtle()
t.shape('turtle')
t.color("red")


for _ in range(15):
        t.pd()
        t.forward(5)
        t.pu()
        t.forward(5)



screen = Screen()
screen.exitonclick()

