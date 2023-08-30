import turtle
import pandas
from state_tracker import StateTracker

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
states_dict = data_dict["state"]
x_dict = data_dict["x"]
y_dict = data_dict["y"]
state_tracker = StateTracker()

while True:
    if state_tracker.score == state_tracker.total:
        state_tracker.write_state("Congrats! You got it all!", 0, 300)
        break

    answer = screen.textinput(title=f"{state_tracker.score}/{state_tracker.total} States Correct", prompt="What is another state name?").title()

    for key in states_dict:
        if answer == states_dict[key]:
            print(x_dict[key], y_dict[key])
            state_tracker.write_state(answer, x_dict[key], y_dict[key])
            state_tracker.update_score()

turtle.mainloop()
