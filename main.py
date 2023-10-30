import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

DELAY = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars_list = []
player = Player()
player.starting_position()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player reach end
    if player.ycor() > 280:
        print("next lvl")
        scoreboard.increase_score()
        player.starting_position()
        car_manager.next_level()


screen.exitonclick()
