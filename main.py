import turtle
from turtle import Screen
from player import Player
from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
from fire_player import Fire_Player
from explosion import Explosion
from brick import Brick
from fire_enemy import Fire_Enemy
import random




screen = Screen()
screen.title('Space Invaders')
screen.bgcolor('black')
screen.tracer(0)

screen.listen()


turtle.register_shape('player.gif')
player = Player((0, -350))


turtle.register_shape('fire_player.gif')

turtle.register_shape('fire_enemy.gif')


turtle.register_shape('explosion.gif')
explosion = Explosion((0, -350))




line = turtle.Turtle()
line.pu()
line.hideturtle()
line.goto(-800,-420)
line.pencolor('#00FFF6')
line.pd()
line.forward(2000)

brick = Brick((-400, -50))
brick1 = Brick((0, -50))
brick2 = Brick((400, - 50))





turtle.register_shape('enemy.gif')
last_line_enemy4 = Enemy((-100, 480))
last_line_enemy5 = Enemy((0, 480))
last_line_enemy6 = Enemy((100, 480))
last_line_enemy7 = Enemy((200, 480))
last_line_enemy3 = Enemy((-200, 480))
last_line_enemy2 = Enemy((-300, 480))
last_line_enemy1 = Enemy((-400, 480))
last_line_enemy = Enemy((-500, 480))
last_line_enemy8 = Enemy((300, 480))

last_list_enemy = [last_line_enemy,last_line_enemy1,last_line_enemy2,last_line_enemy3,last_line_enemy4,
                   last_line_enemy5,last_line_enemy6,last_line_enemy7,last_line_enemy8]

turtle.register_shape('enemy2.gif')
second_line_enemy4 = Enemy2((-100, 380))
second_line_enemy5 = Enemy2((0, 380))
second_line_enemy6 = Enemy2((100, 380))
second_line_enemy7 = Enemy2((200, 380))
second_line_enemy3 = Enemy2((-200,380))
second_line_enemy2 = Enemy2((-300,380))
second_line_enemy1 = Enemy2((-400,380))
second_line_enemy = Enemy2((-500,380))
second_line_enemy8 = Enemy2((300, 380))

second_line_list_enemy = [second_line_enemy,second_line_enemy1,second_line_enemy2,second_line_enemy3,second_line_enemy4,
                   second_line_enemy5,second_line_enemy6,second_line_enemy7,second_line_enemy8]

turtle.register_shape('enemy3.gif')
first_line_enemy4 = Enemy3((-100, 270))
first_line_enemy5 = Enemy3((0, 270))
first_line_enemy6 = Enemy3((100, 270))
first_line_enemy7 = Enemy3((200, 270))
first_line_enemy3 = Enemy3((-200,270))
first_line_enemy2 = Enemy3((-300,270))
first_line_enemy1 = Enemy3((-400,270))
first_line_enemy = Enemy3((-500,270))
first_line_enemy8 = Enemy3((300, 270))

first_List__line_list_enemy = [first_line_enemy,first_line_enemy1,first_line_enemy2,first_line_enemy3,first_line_enemy4,
                   first_line_enemy5,first_line_enemy6,first_line_enemy7,first_line_enemy8]


random_enemy_first_line = random.choice(first_List__line_list_enemy)

enemy_fire = Fire_Enemy((random_enemy_first_line.xcor(), random_enemy_first_line.ycor()), random_enemy_first_line.ycor())
enemy_fire.showturtle()


enemy_fire_second_line = Fire_Enemy((1000, 0),
                                    1000)


enemy_fire_last_line = Fire_Enemy((1000, 0),
                                    1000)




screen.listen()

def left():
    if player.xcor() > -600:

        player.move_left()

def right():
    if player.xcor() < 600:

        player.move_right()

screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

GRAVITY = -0.3
fire = Fire_Player((-1000, -300))


def player_fire():
    global fire

    fire.hideturtle()

    fire = Fire_Player((player.xcor(), -300))
    fire.showturtle()


screen.onkey(player_fire, 'space')



def move_enemy_right():
    first_line_enemy4.move_right()
    first_line_enemy5.move_right()
    first_line_enemy6.move_right()
    first_line_enemy7.move_right()
    first_line_enemy3.move_right()
    first_line_enemy2.move_right()
    first_line_enemy1.move_right()
    first_line_enemy.move_right()
    first_line_enemy8.move_right()

    second_line_enemy4.move_right()
    second_line_enemy5.move_right()
    second_line_enemy6.move_right()
    second_line_enemy7.move_right()
    second_line_enemy3.move_right()
    second_line_enemy2.move_right()
    second_line_enemy1.move_right()
    second_line_enemy.move_right()
    second_line_enemy8.move_right()

    last_line_enemy4.move_right()
    last_line_enemy5.move_right()
    last_line_enemy6.move_right()
    last_line_enemy7.move_right()
    last_line_enemy3.move_right()
    last_line_enemy2.move_right()
    last_line_enemy1.move_right()
    last_line_enemy.move_right()
    last_line_enemy8.move_right()

def move_enemy_left():
    first_line_enemy4.move_left()
    first_line_enemy5.move_left()
    first_line_enemy6.move_left()
    first_line_enemy7.move_left()
    first_line_enemy3.move_left()
    first_line_enemy2.move_left()
    first_line_enemy1.move_left()
    first_line_enemy.move_left()
    first_line_enemy8.move_left()

    second_line_enemy4.move_left()
    second_line_enemy5.move_left()
    second_line_enemy6.move_left()
    second_line_enemy7.move_left()
    second_line_enemy3.move_left()
    second_line_enemy2.move_left()
    second_line_enemy1.move_left()
    second_line_enemy.move_left()
    second_line_enemy8.move_left()

    last_line_enemy4.move_left()
    last_line_enemy5.move_left()
    last_line_enemy6.move_left()
    last_line_enemy7.move_left()
    last_line_enemy3.move_left()
    last_line_enemy2.move_left()
    last_line_enemy1.move_left()
    last_line_enemy.move_left()
    last_line_enemy8.move_left()

def move_enemy_down():
    first_line_enemy4.move_down()
    first_line_enemy5.move_down()
    first_line_enemy6.move_down()
    first_line_enemy7.move_down()
    first_line_enemy3.move_down()
    first_line_enemy2.move_down()
    first_line_enemy1.move_down()
    first_line_enemy.move_down()
    first_line_enemy8.move_down()

    second_line_enemy4.move_down()
    second_line_enemy5.move_down()
    second_line_enemy6.move_down()
    second_line_enemy7.move_down()
    second_line_enemy3.move_down()
    second_line_enemy2.move_down()
    second_line_enemy1.move_down()
    second_line_enemy.move_down()
    second_line_enemy8.move_down()

    last_line_enemy4.move_down()
    last_line_enemy5.move_down()
    last_line_enemy6.move_down()
    last_line_enemy7.move_down()
    last_line_enemy3.move_down()
    last_line_enemy2.move_down()
    last_line_enemy1.move_down()
    last_line_enemy.move_down()
    last_line_enemy8.move_down()

def score_board():
    turtle.hideturtle()
    turtle.goto(500, -490)
    turtle.pencolor('#B5FFD9')
    turtle.clear()
    turtle.write(f'Score {score}', align='center', font=('Arial', 40, 'normal'))

def lose_result():
    game_over = turtle.Turtle()
    game_over.hideturtle()
    game_over.pu()
    game_over.goto(0, 100)

    game_over.pencolor('#D21312')
    game_over.write(f'GAME OVER', align='center', font=('Arial', 45, 'normal'))

def reset_enemy_fire():
    random_enemy_first_line2 = random.choice(first_List__line_list_enemy)
    enemy_fire.new_y = random_enemy_first_line2.ycor()
    enemy_fire.goto(random_enemy_first_line2.xcor(), random_enemy_first_line2.ycor() + 10)
    enemy_fire.showturtle()

def reset_enemy_fire_2():
    if hit_first_line:
        random_enemy_second_line2 = random.choice(second_line_list_enemy)
        enemy_fire_second_line.new_y = random_enemy_second_line2.ycor()
        enemy_fire_second_line.goto(random_enemy_second_line2.xcor(), random_enemy_second_line2.ycor() + 10)

        enemy_fire_second_line.showturtle()


def reset_enemy_fire_3():
    if hit_second_line:
        random_enemy_last_line = random.choice(last_list_enemy)
        enemy_fire_last_line.new_y = random_enemy_last_line.ycor()
        enemy_fire_last_line.goto(random_enemy_last_line.xcor(), random_enemy_last_line.ycor() + 10)

        enemy_fire_last_line.showturtle()



score = 0

n = 1
game_on = True
hit_first_line = False
hit_second_line = False

while game_on:
    screen.update()
    move_enemy_right()



    n += 1
    if n % 42 == 0:
        move_enemy_left()


    enemy_fire.new_y -= enemy_fire.y_move
    enemy_fire.sety(enemy_fire.new_y)

    enemy_fire_second_line.new_y -= enemy_fire_second_line.y_move
    enemy_fire_second_line.sety(enemy_fire_second_line.new_y)

    enemy_fire_last_line.new_y -= enemy_fire_last_line.y_move
    enemy_fire_last_line.sety(enemy_fire_last_line.new_y)

    if enemy_fire.new_y < -550:
        reset_enemy_fire()

    if enemy_fire_second_line.new_y < -550:
        reset_enemy_fire_2()


    if enemy_fire_last_line.new_y < -550:
        reset_enemy_fire_3()






    if brick.distance(enemy_fire) < 55 or brick1.distance(enemy_fire) < 55 or brick2.distance(enemy_fire) < 55:
        enemy_fire.hideturtle()
        reset_enemy_fire()

    if brick.distance(enemy_fire_second_line) < 55 or brick1.distance(enemy_fire_second_line) < 55 or brick2.distance(enemy_fire_second_line) < 55:
        enemy_fire_second_line.hideturtle()
        reset_enemy_fire_2()

    if brick.distance(enemy_fire_last_line) < 55 or brick1.distance(enemy_fire_last_line) < 55 or brick2.distance(enemy_fire_last_line) < 55:
        enemy_fire_last_line.hideturtle()
        reset_enemy_fire_3()


    if enemy_fire.distance(fire) < 20:
        enemy_fire.hideturtle()
        reset_enemy_fire()
        fire.hideturtle()
        fire.goto(1000,0)

    if enemy_fire_second_line.distance(fire) < 20:
        enemy_fire_second_line.hideturtle()
        reset_enemy_fire_2()
        fire.hideturtle()
        fire.goto(1000, 0)

    if enemy_fire_last_line.distance(fire) < 20:

        enemy_fire_last_line.hideturtle()
        reset_enemy_fire_3()
        fire.hideturtle()
        fire.goto(1000, 0)


    if player.distance(enemy_fire) < 25 or player.distance(enemy_fire_second_line) < 25 or player.distance(enemy_fire_last_line) < 25:

        player.hideturtle()
        player.goto(1000,0)
        explosion.goto((player.xcor(), player.ycor()))
        explosion.showturtle()
        lose_result()

        game_on = False





    if n % 5 == 0:
        move_enemy_down()

    if brick.distance(first_line_enemy) < 60 or brick.distance(first_line_enemy1) < 60 or brick.distance(first_line_enemy2) < 60:
        brick.hideturtle()
        brick.goto(1000,0)


    if brick1.distance(first_line_enemy3) < 60 or brick1.distance(first_line_enemy4) < 60 or brick1.distance(first_line_enemy5) < 60:
        brick1.hideturtle()
        brick1.goto(1000,0)

    if brick2.distance(first_line_enemy6) < 60 or brick2.distance(first_line_enemy7) < 60 or brick2.distance(first_line_enemy8) < 60:
        brick2.hideturtle()
        brick2.goto(1000,0)

    if brick.distance(second_line_enemy) < 60 or brick.distance(second_line_enemy1) < 60 or brick.distance(second_line_enemy2) < 60:
        brick.hideturtle()
        brick.goto(1000,0)

    if brick1.distance(second_line_enemy3) < 60 or brick1.distance(second_line_enemy4) < 60 or brick1.distance(second_line_enemy5) < 60:
        brick1.hideturtle()
        brick1.goto(1000,0)

    if brick2.distance(second_line_enemy6) < 60 or brick2.distance(second_line_enemy7) < 60 or brick2.distance(second_line_enemy8) < 60:
        brick2.hideturtle()
        brick2.goto(1000,0)

    if brick.distance(last_line_enemy) < 60 or brick.distance(last_line_enemy1) < 60 or brick.distance(last_line_enemy2) < 60:
        brick.hideturtle()
        brick.goto(1000,0)

    if brick1.distance(last_line_enemy3) < 60 or brick1.distance(last_line_enemy4) < 60 or brick1.distance(last_line_enemy5) < 60:
        brick1.hideturtle()
        brick1.goto(1000,0)

    if brick2.distance(last_line_enemy6) < 60 or brick2.distance(last_line_enemy7) < 60 or brick2.distance(last_line_enemy8) < 60:
        brick2.hideturtle()
        brick2.goto(1000,0)

    if first_line_enemy.distance(player) < 50 or first_line_enemy1.distance(player) < 50 or first_line_enemy2.distance(player) < 50 or first_line_enemy3.distance(player) < 50 or first_line_enemy4.distance(player) < 50 or first_line_enemy5.distance(player) < 50 or first_line_enemy6.distance(player) < 50 or first_line_enemy7.distance(player) < 50 or first_line_enemy8.distance(player) < 50:
        lose_result()

    if second_line_enemy.distance(player) < 50 or second_line_enemy1.distance(player) < 50 or second_line_enemy2.distance(player) < 50 or second_line_enemy3.distance(player) < 50 or second_line_enemy4.distance(player) < 50 or second_line_enemy5.distance(player) < 50 or second_line_enemy6.distance(player) < 50 or second_line_enemy7.distance(player) < 50 or second_line_enemy8.distance(player) < 50:
        lose_result()

    if last_line_enemy.distance(player) < 50 or last_line_enemy1.distance(player) < 50 or last_line_enemy2.distance(player) < 50 or last_line_enemy3.distance(player) < 50 or last_line_enemy4.distance(player) < 50 or last_line_enemy5.distance(player) < 50 or last_line_enemy6.distance(player) < 50 or last_line_enemy7.distance(player) < 50 or last_line_enemy8.distance(player) < 50:
        lose_result()



    # Movement fire player
    fire.new_y += fire.y_move
    fire.sety(fire.new_y)


    if fire.ycor() >= 600:
        fire.hideturtle()
        fire.y_move = 0
        fire.sety(-300)




    # Check first line collision
    if first_line_enemy.distance(fire) < 40:
        first_line_enemy.hideturtle()
        first_line_enemy.goto(1000, 0)
        explosion.goto((first_line_enemy.xcor(), first_line_enemy.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)

        explosion.hideturtle()
        hit_first_line = True
        score += 10



    if first_line_enemy1.distance(fire) < 40:
        first_line_enemy1.hideturtle()
        first_line_enemy1.goto(1000, 0)
        explosion.goto((first_line_enemy1.xcor(), first_line_enemy1.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10



    if first_line_enemy2.distance(fire) < 40:
        first_line_enemy2.hideturtle()
        first_line_enemy2.goto(1000, 0)
        explosion.goto((first_line_enemy2.xcor(), first_line_enemy2.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10



    if first_line_enemy3.distance(fire) < 40:
        first_line_enemy3.hideturtle()
        first_line_enemy3.goto(1000, 0)
        explosion.goto((first_line_enemy3.xcor(), first_line_enemy3.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10



    if first_line_enemy4.distance(fire) < 40:
        first_line_enemy4.hideturtle()
        first_line_enemy4.goto(1000, 0)
        explosion.goto((first_line_enemy4.xcor(), first_line_enemy4.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10


    if first_line_enemy5.distance(fire) < 40:
        first_line_enemy5.hideturtle()
        first_line_enemy5.goto(1000, 0)
        explosion.goto((first_line_enemy5.xcor(), first_line_enemy5.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10


    if first_line_enemy6.distance(fire) < 40:
        first_line_enemy6.hideturtle()
        first_line_enemy6.goto(1000, 0)
        explosion.goto((first_line_enemy6.xcor(), first_line_enemy6.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10


    if first_line_enemy7.distance(fire) < 40:
        first_line_enemy7.hideturtle()
        first_line_enemy7.goto(1000, 0)
        explosion.goto((first_line_enemy7.xcor(), first_line_enemy7.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10


    if first_line_enemy8.distance(fire) < 40:
        first_line_enemy8.hideturtle()
        first_line_enemy8.goto(1000, 0)
        explosion.goto((first_line_enemy8.xcor(), first_line_enemy8.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_first_line = True
        score += 10


    # Check second line collision
    if second_line_enemy.distance(fire) < 40:
        second_line_enemy.hideturtle()
        second_line_enemy.goto(1000, 0)
        explosion.goto((second_line_enemy.xcor(), second_line_enemy.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True

        score += 20


    if second_line_enemy1.distance(fire) < 40:
        second_line_enemy1.hideturtle()
        second_line_enemy1.goto(1000, 0)
        explosion.goto((second_line_enemy1.xcor(), second_line_enemy1.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy2.distance(fire) < 40:
        second_line_enemy2.hideturtle()
        second_line_enemy2.goto(1000, 0)
        explosion.goto((second_line_enemy2.xcor(), second_line_enemy2.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy3.distance(fire) < 40:
        second_line_enemy3.hideturtle()
        second_line_enemy3.goto(1000, 0)
        explosion.goto((second_line_enemy3.xcor(), second_line_enemy3.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)

        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy4.distance(fire) < 40:
        second_line_enemy4.hideturtle()
        second_line_enemy4.goto(1000, 0)
        explosion.goto((second_line_enemy4.xcor(), second_line_enemy4.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy5.distance(fire) < 40:
        second_line_enemy5.hideturtle()
        second_line_enemy5.goto(1000, 0)
        explosion.goto((second_line_enemy5.xcor(), second_line_enemy5.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy6.distance(fire) < 40:
        second_line_enemy6.hideturtle()
        second_line_enemy6.goto(1000, 0)
        explosion.goto((second_line_enemy6.xcor(), second_line_enemy6.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy7.distance(fire) < 40:
        second_line_enemy7.hideturtle()
        second_line_enemy7.goto(1000, 0)
        explosion.goto((second_line_enemy7.xcor(), second_line_enemy7.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    if second_line_enemy8.distance(fire) < 40:
        second_line_enemy8.hideturtle()
        second_line_enemy8.goto(1000, 0)
        explosion.goto((second_line_enemy8.xcor(), second_line_enemy8.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()
        hit_second_line = True
        score += 20


    # Check collision last line

    if last_line_enemy.distance(fire) < 40:
        last_line_enemy.hideturtle()
        last_line_enemy.goto(1000, 0)
        explosion.goto((last_line_enemy.xcor(), last_line_enemy.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30

    if last_line_enemy1.distance(fire) < 40:
        last_line_enemy1.hideturtle()
        last_line_enemy1.goto(1000, 0)
        explosion.goto((last_line_enemy1.xcor(), last_line_enemy1.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy2.distance(fire) < 40:
        last_line_enemy2.hideturtle()
        last_line_enemy2.goto(1000, 0)
        explosion.goto((last_line_enemy2.xcor(), last_line_enemy2.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy3.distance(fire) < 40:
        last_line_enemy3.hideturtle()
        last_line_enemy3.goto(1000, 0)
        explosion.goto((last_line_enemy3.xcor(), last_line_enemy3.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy4.distance(fire) < 40:
        last_line_enemy4.hideturtle()
        last_line_enemy4.goto(1000, 0)
        explosion.goto((last_line_enemy4.xcor(), last_line_enemy4.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy5.distance(fire) < 40:
        last_line_enemy5.hideturtle()
        last_line_enemy5.goto(1000, 0)
        explosion.goto((last_line_enemy5.xcor(), last_line_enemy5.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy6.distance(fire) < 40:
        last_line_enemy6.hideturtle()
        last_line_enemy6.goto(1000, 0)
        explosion.goto((last_line_enemy6.xcor(), last_line_enemy6.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy7.distance(fire) < 40:
        last_line_enemy7.hideturtle()
        last_line_enemy7.goto(1000, 0)
        explosion.goto((last_line_enemy7.xcor(), last_line_enemy7.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    if last_line_enemy8.distance(fire) < 40:
        last_line_enemy8.hideturtle()
        last_line_enemy8.goto(1000, 0)
        explosion.goto((last_line_enemy8.xcor(), last_line_enemy8.ycor()))
        explosion.showturtle()
        fire.hideturtle()
        fire.goto(-1000, 0)


        explosion.hideturtle()

        score += 30


    score_board()

    if brick.distance(fire) < 60 or brick2.distance(fire) < 60 or brick1.distance(fire) < 60:
        fire.hideturtle()
        fire.goto(-1000, 0)











screen.mainloop()