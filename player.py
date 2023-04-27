from turtle import Turtle


class Player(Turtle):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.hideturtle()
        self.pu()
        self.shape('player.gif')
        self.goto((pos))
        self.showturtle()
        self.x_move = 30
        self.new_x = 0

    def move_right(self):
        self.new_x = self.xcor() + self.x_move
        self.goto(self.new_x, self.ycor())

    def move_left(self):
        self.new_x = self.xcor() - self.x_move
        self.goto(self.new_x, self.ycor())

