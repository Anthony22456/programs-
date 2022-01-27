import turtle
import random
import time



screen = turtle.Screen()
screen.bgcolor("light blue")

player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')

player_two = player_one.clone()
player_two.color('black')
player_one.penup()
player_two.penup()
player_two.goto(-300, 200)
player_one.goto(-300, -200)

player_two.goto(300, -250)
player_two.left(90)
player_two.pendown()
player_two.forward(500)
player_two.write('finish!', font=24)

player_two.penup()
player_two.goto(-300, 200)
player_two.right(90)
player_two.pendown()
player_one.pendown()

die =[1, 2, 3, 4, 5, 6]

 for i in range(30):
     if player_two.pos() >= (300, 250):
         print(Player Two Wins)
         break
    elif player_one.pos() >= (300, 250):
         print(Player One Wins)
        break
    else:
        die_roll = random.choice(die)
        player_two.forward(30 * die_roll)
        die_roll2 = random.choice(die)
        player_one.forward(30 * die_roll2)


turtle.done()



