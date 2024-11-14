from turtle import Turtle

UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.starting_positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.starting_position()
        self.head = self.segments[0]

    def starting_position(self):
        for position in self.starting_positions:
            new_square = Turtle(shape='square')
            new_square.penup()
            new_square.color('white')
            new_square.goto(position)
            self.segments.append(new_square)

    def move(self):
        for seg_num in range(len(self.segments) -1 , 0 , -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
