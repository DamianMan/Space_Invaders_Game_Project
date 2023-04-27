from turtle import Turtle


class Fire_Enemy(Turtle):
    def __init__(self, pos, pos_y):
        super(Fire_Enemy, self).__init__()
        self.hideturtle()
        self.shape('fire_enemy.gif')

        self.pu()
        self.goto(pos)
        self.y_move = 8
        self.new_y = pos_y


    def reset_position(self,pos_y):
        self.hideturtle()
        self.goto(pos_y)

