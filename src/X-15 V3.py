55#The X-15
import turtle   ##TURTLE MOD IS GOOD FOR BASIC GAMES
import os
import math
import random
##PYCHARM IS GOOD TO USE TO LEARN##
mainscreen = turtle.Screen()      ##Creating a background variable is mainscreen
mainscreen.bgcolor("black")       ##Colour of background
mainscreen.title("X-15")            ## Title will appear on the top
mainscreen.bgpic("10101.gif")
os.system("afplay lol.wav")
turtle.register_shape("2dedqb.gif")
turtle.register_shape("10101.gif")
turtle.register_shape("102.gif")

pen = turtle.Turtle()                       ##PEN is a pen in reallife we just have to navigate the pen do draw anything
pen.speed(0)                                ## Speed of pen 0 is fastest
pen.color("pink")                               
pen.penup()                                 ##Bring pen up == NO DRAWING
pen.setposition(-280,-280)          ##STARTING position of pen 
pen.down()                                  ## PEN DOWN == DRAWING
pen.pensize(3)                          ## DRAWING PEN SIZE
for side in range(4):
    pen.fd(545)                         ## Forward by 545 units
    pen.lt(90)                          ##Left by 90 units
    pen.hideturtle()                ## No showing of pen

score = 0
## Score of you
scorepen =turtle.Turtle()    ##SCORE PEN TO WRITE SCORES
scorepen.speed(0)           
scorepen.color("white")     
scorepen.penup()
scorepen.setposition(-280,240)
scorestring = "Score: %s" %score   ## % to % brings the Score in the string(Escape code)
scorepen.write(scorestring,False,align="left",font=("Arial",14,"normal")) ##
scorepen.hideturtle()


nameofauth = turtle.Turtle() ## Name of author  
nameofauth.speed(0)
nameofauth.color("white")
nameofauth.penup() ## need this so as to not "draw" but to "write" only penup is only for drawing see line 45
nameofauth.setposition(130,-280)
author = "Made by: Akilan"
nameofauth.write(author,False,align="left",font=("Arial",14,"normal")) ##argument which is my name,followed by wanting it to move or not,align where u want it ot be and font
nameofauth.hideturtle()   ##Hide pen

gamer = turtle.Turtle()  ## YOU IN THIS GAME 
gamer.color("Red")       ##JUST LIKE BELOW U CAN TRY SOME COLOURS ONLY ITS LIMITED
gamer.shape("102.gif")     ##['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle'] try any shape from this try turtle it looks nice
gamer.penup()   ## IT WILL DRAW THE MOVEMENT OF ME if i dont penup try it alt 3 this function
gamer.speed(0)   ##NOTE: this the drawing speed
gamer.setposition(0,-255)
gamer.setheading(90)  ### Where the triangle face


numofdest = 5
destroyers = []

for i in range(numofdest):
    destroyers.append(turtle.Turtle())   ## This function add turtle.turle() into destroyers

for destroyer in destroyers:
    destroyer.color("Pink")
    destroyer.shape("10101.gif")    ## Change shape as much as you want
    destroyer.penup()
    destroyer.speed(0)       ## NOTE: This is the spawn speed
    x = random.randint(-200,200) ## RANDOM SPAWN of destroyers in xcor/ STARTING SPAWN
    y = random.randint(100,250)  ## RANDOM SPAWN of destroyers in ycor/ STARTING SPAWN
    destroyer.setposition(x,y)
    destroyerspeed = 2 




#Missile
missile = turtle.Turtle() ## GUN
missile.color("green")
missile.shape("2dedqb.gif")
missile.penup()
missile.speed(0)
missile.setheading(90)
missile.hideturtle()

missilespeed = 25


missilestate = "solid" ## MORE DESCRIPTION ALL THE WAY AT END ABOUT THIS







gamerspeed = 20
#MAKING THE PLAYER MOVE EVERYWHERE
def left():
    x =gamer.xcor()
    x -= gamerspeed
    if x < -260:              ##BORDER LIMIT TO STOP YOU FROM GOING OUTSIDE
        x = -260
    gamer.setx(x)        ## SET COR

def right():
    x =gamer.xcor()
    x += gamerspeed
    if x > 250:             ## OTHER SIDE OF BORDER
        x = 250
    gamer.setx(x)

def missileshot():        ## MISSILE LEAVES YOU APPROACHING ENEMY
    global missilestate #CAN READ AND WRITE#EDITABLE
    if missilestate == "solid":
        missilestate = "liquid"
        
        x = gamer.xcor()
        y = gamer.ycor()+ 10  # MOVE HORIZONTALLY UPWARDS
        missile.setposition(x,y)
        missile.showturtle()  # SHOW THE MISSILE 

def isdestroyed(a1,a2):  ##turtle 1 and turtle 2
    dist = math.sqrt(math.pow(a1.xcor()-a2.xcor(),2)+math.pow(a1.ycor()-a2.ycor(),2)) ## DISTANCE BETWEEN MISSILE AND ENEMY missile is a1 a2 is enemy
    ### ^ Pythagoras Theoram So as to find  longest staight line dist in units (Guess only not sure lol)
    if dist < 20:  ## AS LONG AS NEAR 20 UNITS OF RADIUS ENEMY IT WILL ANNILATE THE ENEMY
       return True
    else:
        return False

#KEY BINDINGS ## Binds function with keyboard keys
turtle.listen()
turtle.onkey(left,"Left")  ##left is function "Left" is key##
turtle.onkey(right,"Right")
turtle.onkey(missileshot,"space")

#LOOP#EVERYTHING HERE IS IMPORTANT# CHEESE IN PIZZA IMPORTANT##
while True:
    for destroyer in destroyers:
        o =destroyer.xcor()
        o += destroyerspeed
        destroyer.setx(o ) ##Moving destroyer vertically set new x as x

        #MAKING ENEMY MOVE EVERYWHERE
        if destroyer.xcor() >250:  ## REACHES BORDER
            for k in destroyers:
                y = k.ycor()
                y -= 40   ##Moves downwards by 40 units
                k.sety(y) ## set new y as y cor
            destroyerspeed *= -1  ##makes speed  - so that it will make x cor - so the enemy will move backwards

        if destroyer.xcor() < -260: ## REACHES OTHER SIDE OF BORDER
            for k in destroyers:
                y = k.ycor()
                y -= 40
                k.sety(y)
            destroyerspeed *= -1

        if isdestroyed(missile, destroyer):
            missile.hideturtle()
            missilestate = "solid"
            missile.setposition(0, -500)  ## BACK IN YOU
            x = random.randint(-200, 200)## RANDOM SPAWN of destroyers in ycor/ DEADSPAWN
            y = random.randint(100, 250)## RANDOM SPAWN of destroyers in ycor/ DEAD SPAWN
            destroyer.setposition(x, y)
            score += 10
            scorestring = "Score: %s" % score  ## SCORE
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal")) ##SCORE INPUT IN GAME
            scorepen.hideturtle()

        if isdestroyed(gamer, destroyer): ##IF U DIE
            gamer.hideturtle()
            print("GAME OVER YOUR TOTAL POINT IS %s"%score)
            break ##BREAK LOOP GO TO THE END TO ln202

    if missilestate == "liquid":
        y = missile.ycor()
        y += missilespeed   ##MISSILE MOVEMENT UPWARDS
        missile.sety(y)


    if missile.ycor() > 251:  ## MISSILE GO BACK IN YOU AFTER IT EXITS THE TOP BORDER
        missile.hideturtle()  
        missilestate = "solid"   


###SOLID MEANS IT IS IN YOU THE GAMER IT HASNT BEEN SHOT  IT IS USE DO DESCRIBE
###THE STATE OF MISSILE
### SO IF LIQUID MEANS IT LEFT YOU AND HEADS TO ENEMY
###IF SHOT AND KILLED IT BECOMES GAS
###GAS IS OPTIONAL
### YOU CAN USE OTHER VARIABLES like (1,2,3),(baby,kid,adult) just to describe the state of the missile,not a must to use solid liquid gas









delay = input("Press enter to exit:")







