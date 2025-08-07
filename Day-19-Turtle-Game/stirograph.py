import turtle as x
import random

t = x.Turtle()
t.speed("fastest")
x.colormode(255)
directions = [0, 90, 180, 270]

def rand_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)
    
for _ in range(100):
    t.color(rand_col())
    t.circle(100)
    t.tilt(100)
    t.setheading(t.heading() + 5)

    


screen = x.Screen()
screen.exitonclick()