import pandas
from turtle import Turtle

FONT = ("Arial", 8, "normal")
ALIGN = "center"


class StateTracker(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")

        self.data = None
        self.all_states = []
        self.read_data()
        self.correct_answers = []
        self.total = len(self.all_states)
        self.score = 0

    def read_data(self):
        # Read csv using pandas
        self.data = pandas.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()

    def check_answer(self, answer):
        # Check if user guess is in the states list, if yes write state on map
        if answer in self.all_states:
            data = self.data
            state = data[data.state == answer]
            self.write_state(answer, int(state.x.iloc[0]), int(state.y.iloc[0]))
            self.correct_answers.append(answer)
            self.score = len(self.correct_answers)

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(arg=name, font=FONT, align=ALIGN)

    def missing_states(self):
        missing_list = [state for state in self.all_states if state not in self.correct_answers]
        missing_data = pandas.DataFrame(missing_list)
        missing_data.to_csv("states_to_learn.csv")
