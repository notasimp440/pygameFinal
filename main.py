import turtle as tur
import tkinter as tk
import time








tur.setup
wn = tur.Screen

#game start 
sc = tur.Screen() 
sc.setup(1500,1500) 


#our pics
cry_man = 'kms.gif'
rammy = 'R2.gif'

#all the mumbo jumbo
tur.addshape(rammy)
tur.addshape(cry_man)

#def curstomer_order():





    




#button mapping
def player_interact():
    if (player.xcor() <= -300 and player.xcor() >= -350  and player.ycor() >= -20 and player.ycor() <= 90):
        grabChips.write("grabbed chips", font=("Arial", 32, "normal"))
        time.sleep(0.3)
        grabChips.clear()


def player_right():
    if player.xcor() < 300:
        for i in range(5):
            player.goto(player.pos() + (6, 0))

def player_left():
    if player.xcor() > -300:
        for i in range(5):
            player.goto(player.pos() + (-6, 0))


def player_down():
    #print(player.ycor())
    if player.ycor() > -400:
        for i in range(5):
            player.goto(player.pos() + (0, -5))

def player_up():
    #print(player.ycor())
    if player.ycor() < 90:
        for i in range(5):
            player.goto(player.pos() + (0, 6))



#just random stuff that couldn't really go anywhere else
grabChips = tur.Turtle() 
grabChips.penup()
grabChips.hideturtle()
grabChips.goto(-350,110)




#customer init
customer = tur.Turtle()
customer.shape(cry_man)
customer.penup()
customer.speed(200)
customer.hideturtle()
customer.goto(0, 350)

#player init
player = tur.Turtle()
player.shape(rammy)
player.shapesize(1,1,1)
player.penup()
player.goto(0,0)
playerPos = player.pos()

#take order
tkorder = tur.Turtle()
tkorder.shape("square")
tkorder.penup()
tkorder.goto(0,130)
tkorder.shapesize(2,2)


#player zone
wall = tur.Turtle()
wall.speed(0)
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

#stove set-up
stove = tur.Turtle()
stove.speed(0)
stove.hideturtle()
stove.penup()
stove.goto(-300,90)
stove.pendown()
stove.goto(-300, -20)
stove.goto(-350,-20)
stove.goto(-350,90)
stove.goto(-300,90)
stove.fillcolor('black')

#player event
tur.listen()
tur.onkey(player_right,'Right')
tur.onkey(player_left, 'Left')
tur.onkey(player_down, 'Down')
tur.onkey(player_up, 'Up')
tur.onkey(player_interact, "e")

        
    


tur.mainloop()
