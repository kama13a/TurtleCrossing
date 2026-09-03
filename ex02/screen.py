import time
from turtle import Turtle, Screen
from object_turtle import Object
from car_manager import CarManager
from message import Message
from level import Level

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

tim = Object()
color_list = ["yellow", "red", "black", "purple", "blue", "green",]

car_manager = CarManager()
text = Message()
level = Level()
screen.listen()
screen.onkey(tim.move, "w")
screen.onkey(tim.backwards, "s")
screen.onkey(tim.left_forward, "a")
screen.onkey(tim.right_forward , "d")

game_on = True

while game_on:
    car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    if car_manager.detect_collision(tim):
        text.write_message()
        game_on = False
        break
    if tim.ycor() > 280:
        tim.restart()
        level.level_up()
        car_manager.speed_up()

    screen.update()









screen.exitonclick()
