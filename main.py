import turtle as tur
tur.setup(1500,1500)
wn = tur.Screen()

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
player.forward(100)


while True:
    tur.listen

    tur.onkey(player_right, 'Right')




    wn.mainloop()
