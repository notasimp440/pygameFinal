import turtle as tur
import tkinter as tk







tur.setup
wn = tur.Screen

#our pics
cry_man = 'kms.gif'
rammy = 'R2.gif'

#all the mumbo jumbo
tur.addshape(rammy)
tur.addshape(cry_man)


#button mapping
def player_right():
    for i in range(5):
        player.goto(player.pos() + (6, 0))

def player_left():
    player.goto(player.pos() + (-30, 0))


def player_down():
    player.goto(player.pos() + (0, -30))

def player_up():
    player.goto(player.pos() + (0, 30))

#player init
player = tur.Turtle()
player.shape(rammy)
player.shapesize(1,1,1)
player.penup()
player.goto(0,0)

#player zone
wall = tur.Turtle()
wall.speed(200)
wall.hideturtle()
wall.penup()
wall.goto(0,90)
wall.pendown()
wall.goto(300,90)
wall.goto(-300,90)
wall.goto(-300,-90)
wall.goto(-300,-400)
wall.pencolor('white')
wall.goto(300,-400)
wall.pencolor('black')
wall.goto(300,90)


#player event
tur.listen()
tur.onkey(player_right,'Right')
tur.onkey(player_left, 'Left')
tur.onkey(player_down, 'Down')
tur.onkey(player_up, 'Up')

tur.mainloop()


