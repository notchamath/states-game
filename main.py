import turtle
from state_tracker import StateTracker

# Set up the Screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set up the map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_tracker = StateTracker()

while True:
    # End game if user get all states correctly
    if state_tracker.score == state_tracker.total:
        state_tracker.write_state("Congrats! You got it all!", 0, 300)
        break

    # Get guess from user, make it Pascal case
    answer = screen.textinput(title=f"{state_tracker.score}/{state_tracker.total} States Correct",
                              prompt="What is another state name?").title()

    # End game if user types exit, produce a list of states they missed
    if answer == "Exit":
        state_tracker.missing_states()
        break

    # Check if user answer is correct
    state_tracker.check_answer(answer)

turtle.mainloop()
