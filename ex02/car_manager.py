from turtle import Turtle
import random



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 5

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(self.color_of_cars())
            new_car.goto(280, self.location_of_cars())
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def color_of_cars(self):
        color_list = ["red", "blue", "green", "yellow", "orange", "purple"]
        return random.choice(color_list)

    def location_of_cars(self):
        return random.randint(-280, 220)

    def detect_collision(self, player):
        for car in self.all_cars:
            if player.distance(car) < 25:
                return True
        return False

    def speed_up(self):
        self.speed += 2








