import pandas
from turtle import Turtle

FONT = ("Arial", 8, "normal")
ALIGN = "center"
TOTAL_STATES = 50


class StateTracker(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.total = TOTAL_STATES
        self.correct_answers = []

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(arg=name, font=FONT, align=ALIGN)
        self.update_score(name)

    def update_score(self, name):
        self.score += 1
        self.correct_answers.append(name)

    def missing_states(self, all_states):
        missing_list = []
        for state in all_states:
            if state not in self.correct_answers:
                missing_list.append(state)

        missing_data = pandas.DataFrame(missing_list)
        missing_data.to_csv("states_to_learn.csv")
