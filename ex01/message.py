from turtle import Turtle

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_message(self):
        self.write("Game Over", False, "center", ("Arial", 30, "normal"))