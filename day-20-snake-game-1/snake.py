from turtle import Turtle

s = [(0,0), (-20,0), (-40,0)]
move = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in s:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(pos)
            self.segments.append(new)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(move)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)
    def left(self):
        if self.segments[0].heading() != 00:

            self.segments[0].seth(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)



