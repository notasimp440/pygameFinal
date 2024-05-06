import turtle as tur

tur.setup

#our pics
cry_man = 'kms.gif'
rammy = 'rammy.gif'

#all the mumbo jumbo
wn.addshape(rammy)
wn.addshape(cry_man)

def player_right():
    player.forward(20)

#plyaer
player = tur.Turtle()
player.shape(rammy)
player.shapesize(1,1,1)

wn.listen

wn.onkey(player_right, 'Right')


