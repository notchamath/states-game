from turtle import Turtle

FONT = ("Arial", 8, "normal")
ALIGN = "center"


class StateNames(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")

    def write_state(self, name, x, y):
        self.goto(x, y)
        self.write(arg=name, font=FONT, align=ALIGN)
