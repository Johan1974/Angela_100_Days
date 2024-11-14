import random
from random import randint
from turtle import Turtle, Screen
from screeninfo import get_monitors


# Get the screen resolution of the primary monitor
monitor = get_monitors()[0]  # Assuming the first monitor is the primary one
screen_width = monitor.width
screen_height = monitor.height


turtle = Turtle()
screen = Screen()
screen.setup(screen_width,screen_height)
screen.colormode(255)

turtle.shape('turtle')
turtle.pensize(10)

def random_color_generator():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw():
    turtle.pencolor(random_color_generator())
    turtle.color(random_color_generator())
    turtle.setheading(randint(0,360))
    turtle.forward(30)
    screen.ontimer(draw, 100)

draw()

screen.exitonclick()
