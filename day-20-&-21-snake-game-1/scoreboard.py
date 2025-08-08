from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,175)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "bold"))

    def gameOver(self):
        self.clear()
        self.write(f"Game Over! You got a score of {self.score}", False, "center", ("Arial", 15, "bold"))

        
    def increase(self):
        self.score += 1
        self.clear()
        self.update()

        

