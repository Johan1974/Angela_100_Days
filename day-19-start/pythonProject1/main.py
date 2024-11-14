import turtle
from os import MFD_ALLOW_SEALING
from turtle import Turtle, Screen
from random import random, randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win  the race? Enter a color')

colors = ['red','orange','yellow','green','blue','purple']
turtles = {}


start_pos = 0 - (screen.window_height() / 2)
part = screen.window_height() / 7

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    start_pos += part
    turtle.setpos(- (screen.window_width()  / 2 ) + 20  , start_pos )
    turtles[color] = turtle


finish = False

while not finish:
    for color in colors:
        turtles[color].forward(randint(-5,10))
        x,y = turtles[color].pos()
        if x > (screen.window_width() / 2) - 30:
            finish = True
            if user_bet == color:
                print(f"You have won! ", end='')
            else:
                print(f"You have lost! ", end='')
            print(f"The {color} turtle is the winner!")



screen.exitonclick()
