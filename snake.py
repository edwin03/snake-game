from turtle import Turtle

class Snake:
    def __init__(self, position):
        self = Turtle("square")
        self.penup()
        self.color("white")
        self.goto(position)
    
    def move(self, segments):
        for seg in range(len(segments)-1, 0, -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)