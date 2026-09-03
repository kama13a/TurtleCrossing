from turtle import Turtle

class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green", "red")
        self.setheading(90)
        self.penup()
        self.goto(0,-280)



    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def backwards(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_forward(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right_forward(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def restart(self):
        self.goto(0, -280)

