from turtle import Turtle


class Explosion(Turtle):
    def __init__(self, pos):
        super(Explosion, self).__init__()
        self.hideturtle()
        self.shape('explosion.gif')

        self.pu()
        self.goto((pos))
