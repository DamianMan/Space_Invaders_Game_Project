from turtle import Turtle


class Brick(Turtle):
    def __init__(self, pos):
        super(Brick, self).__init__()
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=6)
        self.color('#28DF99')
        self.speed(0)

        self.pu()
        self.goto((pos))
        self.showturtle()