from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-180, 250)
        self.level_up()

    def level_up(self):
            self.level += 1
            self.upgrade()



    def upgrade(self):
        self.clear()
        self.write(f"Level {self.level}", False, "right", ("Courier", 20, "normal"))
