import turtle as tur







tur.setup
wn = tur.Screen

#our pics
cry_man = 'kms.gif'
rammy = 'rammy.gif'

#all the mumbo jumbo
tur.addshape(rammy)
tur.addshape(cry_man)


#button mapping
def player_right():
    player.goto(player.pos() + (30, 0))

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

#player bar
wall = tur.Turtle()
wall.penup()
wall.goto(250,250)
wall.pendown()
wall.forward(250)
wall.right(250)
wall.penup()
wall.goto(-250, 250)



#player event
tur.listen()
tur.onkey(player_right,'Right')
tur.onkey(player_left, 'Left')
tur.onkey(player_down, 'Down')
tur.onkey(player_up, 'Up')

tur.mainloop()


