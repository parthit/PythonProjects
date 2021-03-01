from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250 )
        self.show_level()

    def show_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)



