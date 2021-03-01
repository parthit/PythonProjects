from turtle import Turtle, Screen
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment(position=(0,0), flag=False)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def add_segment(self, position, flag):
        x_cor = 0
        y_cor = 0
        snake_body_segment = Turtle(shape="square")
        snake_body_segment.color("white")
        snake_body_segment.penup()
        if flag == False:
            snake_body_segment.goto(x_cor, y_cor)
        else:
            snake_body_segment.goto(position)
        self.snake_body.append(snake_body_segment)
        x_cor -= 20

    def extend(self):
        self.add_segment(position=self.snake_body[-1].position(), flag=True)


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






