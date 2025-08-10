from turtle import Turtle

class Pin(Turtle):
    def __init__(self,x,y,state):
        super().__init__
        self.x = x
        self.y = y
        self.state = state
    
    def move(self):
        new = Turtle("square")
        new.hideturtle()
        new.penup()
        new.goto(self.x,self.y)
        new.write(self.state)
        
