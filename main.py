import turtle
import pandas
from state_names import StateNames

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
state_names = StateNames()

is_game_on = True

while is_game_on:
    answer = screen.textinput(title="Guess a State", prompt="What is another state name?").title()

    for key in states_dict:
        if answer == states_dict[key]:
            print(x_dict[key], y_dict[key])
            state_names.write_state(answer, x_dict[key], y_dict[key])

turtle.mainloop()
