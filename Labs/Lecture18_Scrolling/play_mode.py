import random
import json
import os

from pico2d import *
import game_framework
import game_world
<<<<<<< HEAD
from ball import Ball
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b

import server
from boy import Boy

# fill here
from background import FixedBackground as Background
<<<<<<< HEAD
from background import FixedBackground as Background
=======


>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)


<<<<<<< HEAD
=======

>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
def init():
    server.background = Background()
    game_world.add_object(server.background, 0)
    server.boy = Boy()
    game_world.add_object(server.boy, 1)
<<<<<<< HEAD
    game_world.add_collision_pair('boy:ball', server.boy, None)

    balls = [Ball() for _ in range(100)]
    for ball in balls:
        game_world.add_object(ball, 1)
        game_world.add_collision_pair('boy:ball', None, ball)
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

<<<<<<< HEAD

=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

<<<<<<< HEAD

def pause():
    pass


def resume():
    pass
=======
def pause():
    pass

def resume():
    pass



>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
