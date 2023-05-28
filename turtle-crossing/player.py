from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def back(self):
        self.home()