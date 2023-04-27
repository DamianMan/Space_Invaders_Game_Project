from turtle import Turtle


class Fire_Player(Turtle):
    def __init__(self, pos):
        super(Fire_Player, self).__init__()
        self.hideturtle()
        self.shape('fire_player.gif')

        self.pu()
        self.goto(pos)
        self.y_move = 13
        self.new_y = -300


    def reset_position(self):
        self.sety(-300)
        self.hideturtle()



