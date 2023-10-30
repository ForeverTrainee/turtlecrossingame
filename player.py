from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # new_player = Turtle()
        self.shape("turtle")
        self.y_move = 10
        self.left(90)

    def starting_position(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
