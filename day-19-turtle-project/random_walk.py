import turtle as x
import random

t = x.Turtle()
t.speed(0)
x.colormode(255)
directions = [0, 90, 180, 270]
t.pensize(10)

def rand_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)
    
for _ in range(100):
    t.color(rand_col())
    x = random.choice(directions)
    t.setheading(x)
    t.forward(10)


screen = x.Screen()
screen.exitonclick()