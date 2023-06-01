import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle
turtle = Player()
# listen to event
screen.listen()
screen.onkey(turtle.move, "Up")

# car
car = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    if turtle.ycor() > 290:
        turtle.back()

    car.generate_car()
    car.move()

    # detect the distance (collision)
    for each in car.cars:
        if each.distance(turtle) < 20:
            game_is_on = False
            print("Game Over")
