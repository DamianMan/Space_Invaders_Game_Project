from turtle import Turtle


class Enemy2(Turtle):
    def __init__(self, pos):
        super(Enemy2, self).__init__()
        self.hideturtle()
        self.shape('enemy2.gif')
        self.speed(0)

        self.pu()
        self.goto((pos))
        self.showturtle()
        self.new_y = 0
        self.new_x = 0
        self.x_move = 5
        self.y_move = 1

    def move_right(self):
        self.new_x = self.xcor() + self.x_move
        self.goto(self.new_x, self.ycor())

    def move_left(self):
        self.x_move *= -1

    def move_down(self):
        self.new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), self.new_y)
