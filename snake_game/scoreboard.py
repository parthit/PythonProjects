from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scorebaord()
        self.hideturtle()

    def update_scorebaord(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.read_highscore()}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if int(self.score) > int(self.highscore):
            self.set_highscore(self.score)
        self.score = 0
        self.update_scorebaord()

    def increase_score(self):
        self.score += 1
        self.update_scorebaord()

    def read_highscore(self):
        with open(file='highscore.txt', mode='r') as highscore:
            return highscore.read()


    def set_highscore(self, score):
        with open(file='highscore.txt', mode='w') as highscore:
            highscore.write(str(score))


    # def game_over(self):
    #     self.goto(0 , 0)
    #     self.write(f"Game Over.", align="center", font=("Courier", 24, "normal"))