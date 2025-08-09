from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day-24-files/save.txt") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.penup()
        self.goto(0,175)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 15, "bold"))

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day-24-files/save.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update()
        
    def increase(self):
        self.score += 1
        self.clear()
        self.update()

        

