import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
<<<<<<< HEAD
    global balls
    balls = [Ball(random.randint(100, 1500), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    # 충돌 정보를 등록
    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('zombie:ball', None, ball)

    #zombie 5 add
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    for zombie in zombies:
        game_world.add_collision_pair('zombie:ball', zombie, None)
=======


>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd


def finish():
    game_world.clear()
    pass


def update():
<<<<<<< HEAD
    game_world.update()  # 소년과 볼 위치가 다 업데이트 완료
    game_world.handle_collisions()
=======
    game_world.update()
    # fill here

>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd

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

>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
