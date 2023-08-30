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

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(arg=name, font=FONT, align=ALIGN)

    def update_score(self):
        self.score += 1
