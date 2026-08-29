import time
from turtle import Turtle, Screen
from object_turtle import Object

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

tim = Object()

screen.listen()
screen.onkey(tim.move, "w")
screen.onkey(tim.backwards, "s")
screen.onkey(tim.left_forward, "a")
screen.onkey(tim.right_forward , "d")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)




screen.exitonclick()
