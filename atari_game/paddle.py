from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=xcor, y=ycor)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)


