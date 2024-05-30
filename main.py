import turtle as tur
import tkinter as tk
import time
from random import *








tur.setup
wn = tur.Screen()

#game start 
sc = tur.Screen() 
sc.setup(1500,1500) 
sc.bgpic()


#our pics
cry_man = 'kms.gif'
rammy = 'R2.gif'







#all the mumbo jumbo
num = 0
game_len = 5
tur.addshape(rammy)
tur.addshape(cry_man)
order_taken = bool
uni_size = ["Arial", 20, "normal"]



txt4order = tur.Turtle()
txt4order.speed(0)
txt4order.hideturtle()
txt4order.penup()
txt4order.goto(-130,150)


#scores
orders_given = 0
chips = 0

ui1 = tur.Turtle()
ui2 = tur.Turtle()
ui1.speed(0)
ui2.speed(0)
ui1.hideturtle() 
ui2.hideturtle()

ui1.penup()
ui2.penup()

ui1.goto(-200, 250)
ui2.goto(-200, 230)

ui1.write("orders given " + str(orders_given), font= uni_size)
ui2.write("chips : " + str(chips), font= uni_size)


def player_location_check(x1, x2, y1, y2):
    if (player.xcor() <= x2 and player.xcor() >= x1 and player.ycor() >= y1 and player.ycor() <= y2):
        return True
    else:
        return False
    
    

    
#event handlers
def give_order():
    global order_taken
    global want_chips
    global orders_given
    global chips
    if (player_location_check(-10, 5, 50, 130) == True and order_taken == True):
        if chips == want_chips:
            order_taken = False
            chips -= want_chips
            orders_given += 1
            ui1.clear()
            ui1.write("orders given " + str(orders_given), font= uni_size)
            
            customer.goto(0, 550)
            tkorder.write("Ready to take order?", align= "left",  font= ("arial", 30, "normal"))
            return order_taken
        else:
            tur.speed(0)
            tur.hideturtle()
            tur.penup()
            tur.goto(-100,150)
            tur.write("thats not what i ordered!", font= uni_size, align= "left" )
            time.sleep(1)
            tur.clear()



    else:
        pass 

        
        



def take_order():
    global order_taken, want_chips
    global chips
    if (player_location_check(-10, 5, 50, 130)) and order_taken != True:
        want_chips = randint(1,3)
        tkorder.clear()
        tkorder.hideturtle()
        customer.showturtle()
        customer.goto(0,130)
        txt4order.write("i want" + str(want_chips) + "chips", font= uni_size)
        time.sleep(1)
        txt4order.clear()
        order_taken = True
        return order_taken 


    




#button mapping
def player_interact():
    global chips
    global ui1
    global ui2
    if (player.xcor() <= -300 and player.xcor() >= -350  and player.ycor() >= -20 and player.ycor() <= 90):
        grabChips.write("grabbed chips", font=("Arial", 32, "normal"))
        time.sleep(0.1)
        chips += 1
        ui2.clear()
        ui2.write("chips : " + str(chips), font= uni_size)
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
    print(player.ycor())
    if player.ycor() < 90:
        for i in range(5):
            player.goto(player.pos() + (0, 6))



#just random stuff that couldn't really go anywhere else
grabChips = tur.Turtle() 
grabChips.penup()
grabChips.hideturtle()
grabChips.goto(-350,110)
chips = 0





#customer init
customer = tur.Turtle()
customer.shape(cry_man)
customer.penup()
customer.speed(2)
customer.hideturtle()
customer.goto(0, 500)

#player init
player = tur.Turtle()
player.shape(rammy)
player.shapesize(1,1,1)
player.penup()
player.goto(0,0)
playerPos = player.pos()

#ready to order.text
tkorder = tur.Turtle()
tkorder.hideturtle()
tkorder.penup()
tkorder.goto(-130,130)
tkorder.write("Ready to take order?", align= "left",  font= ("arial", 30, "normal"))


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
tur.onkey(take_order, "q")
tur.onkey(give_order,"g")

        
    


sc.title('FINISHED! FINAL SCORE: {}'.format(num))

tur.mainloop()
sc.update()

