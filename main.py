import turtle as tur
import tkinter as tk








tur.setup
wn = tur.Screen

#game start 
sc = tur.Screen() 
sc.setup(1500,1500) 
tur.textinput("YOU READY?") 

#our pics
cry_man = 'kms.gif'
rammy = 'R2.gif'

#all the mumbo jumbo
tur.addshape(rammy)
tur.addshape(cry_man)



#button mapping
def player_interact():
    if (player.xcor() <= -300 and player.xcor() >= -350  and player.ycor() >= -20 and player.ycor() <= 90):
        print("grabbed chips")



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

#stove set-up
stove = tur.Turtle()

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


