import turtle
import pandas
from state_tracker import StateTracker

# Set up the Screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set up the map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read csv using pandas
data = pandas.read_csv("50_states.csv")

# Turn csv into a dict
data_dict = data.to_dict()
states_dict = data_dict["state"]
x_dict = data_dict["x"]
y_dict = data_dict["y"]

state_tracker = StateTracker()

while True:
    # End game if user get all states correctly
    if state_tracker.score == state_tracker.total:
        state_tracker.write_state("Congrats! You got it all!", 0, 300)
        break

    # Get guess from user, make it Pascal case
    answer = screen.textinput(title=f"{state_tracker.score}/{state_tracker.total} States Correct", prompt="What is another state name?").title()

    # Check if user guess is in the states list
    for key in states_dict:
        if answer == states_dict[key]:
            state_tracker.write_state(answer, x_dict[key], y_dict[key])
            state_tracker.update_score()

turtle.mainloop()
