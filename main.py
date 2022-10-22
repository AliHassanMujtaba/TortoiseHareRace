import time
import turtle
import random

drawer = turtle.Turtle()
hare = turtle.Turtle()
tortoise = turtle.Turtle()

# Write message at the top#
drawer.penup()
drawer.setpos(-150, 200)
drawer.pendown()
drawer.write('ON YOUR MARK.... GET SET.... GO!!!! \n AND THEY\'RE OFF', font=('Arial', 16, 'normal'))

# Draw starting and finish line#
drawer.penup()
drawer.setpos(-100, 100)
drawer.pendown()
drawer.right(90)
drawer.forward(200)
drawer.penup()
drawer.setpos(100, 100)
drawer.pendown()
drawer.forward(200)
# Write Start end#
drawer.penup()
drawer.setpos(-120, 120)
drawer.pendown()
drawer.write('Start')
drawer.penup()
drawer.setpos(120, 120)
drawer.pendown()
drawer.write('End')
drawer.hideturtle()

#Resetting the Position of hare and tortoise#
hare.shape('arrow')
tortoise.shape('turtle')
hare.penup()
hare.setpos(-100,50)
tortoise.penup()
tortoise.setpos(-100,0)


def tortoise_movement():
    num = random.randint(1,10)
    if num >=1 and num <= 5:
        tortoise.forward(3)
    elif num >= 6 and num<= 7:
        tortoise.backward(5)
    else:
        tortoise.forward(1)
    return tortoise.pos()

def hare_movement():
    num = random.randint(1,10)
    if num >= 1 and num <=2:
        a = 0
    elif num >= 3 and num <= 4:
        hare.forward(7)
    elif num == 5:
        hare.backward(10)
    elif num >=6 and num <= 8:
        hare.forward(1)
    else:
        hare.backward(2)
    return hare.pos()

count = 0
race_end = False
while not race_end:
    tortoise_pos = tortoise_movement()
    hare_pos = hare_movement()
    count+=1
    if tortoise_pos <= (-100,0):
        tortoise.setpos(-100,0)
    if hare_pos <= (-100,50):
        hare.setpos(-100,50)
    if tortoise_pos >= (100,0):
        drawer.penup()
        drawer.setpos(-150,-200)
        drawer.pendown()
        drawer.write('Tortoise WON !!!!!!',font=('Arial',16,'normal'))
        race_end = True
    if hare_pos >= (100,50):
        drawer.penup()
        drawer.setpos(-150, -200)
        drawer.pendown()
        drawer.write('Hare WON !!!!!!', font=('Arial', 16, 'normal'))
        race_end = True

drawer.penup()
drawer.setpos(200,-200)
drawer.write(f'Time of race : {count}')
time.sleep(3)

