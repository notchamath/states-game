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
all_states = data.state.to_list()

state_tracker = StateTracker()

while True:
    # End game if user get all states correctly
    if state_tracker.score == state_tracker.total:
        state_tracker.write_state("Congrats! You got it all!", 0, 300)
        break

    # Get guess from user, make it Pascal case
    answer = screen.textinput(title=f"{state_tracker.score}/{state_tracker.total} States Correct",
                              prompt="What is another state name?").title()

    # End game if user types exit
    if answer == "Exit":
        state_tracker.missing_states(all_states)
        break

    # Check if user guess is in the states list, if yes write state on map
    if answer in all_states:
        state = data[data.state == answer]
        state_tracker.write_state(answer, int(state.x.iloc[0]), int(state.y.iloc[0]))

turtle.mainloop()
