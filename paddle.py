from turtle import Turtle

WIDTH = 5
HEIGHT = 1


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT, outline=None)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
