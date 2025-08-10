import turtle
import pandas
from pin import Pin

screen = turtle.Screen()
screen.title("USA States Guessing Game")

image = "day-25-pandas-library/usa-state-guess/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def coord(x,y):
    print(x,y)

turtle.onscreenclick(coord)

data = pandas.read_csv("day-25-pandas-library/usa-state-guess/50_states.csv")

states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(f"{len(guessed)}/50 States", "Whats the next state's name?").title()

    if answer == "":
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)
        new = pandas.DataFrame(missing)
        new.to_csv("day-25-pandas-library/usa-state-guess/missing_states.csv")
        break
    if answer in states and answer not in guessed:
        guessed.append(answer)
        location = data[data.state == answer]
        xcoord = int(location.x.item())
        ycoord = int(location.y.item())
        new = Pin(xcoord, ycoord, answer)
        new.move()

