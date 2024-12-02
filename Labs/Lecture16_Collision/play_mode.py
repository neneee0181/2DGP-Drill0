import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
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
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
<<<<<<< HEAD
<<<<<<< HEAD
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
=======


>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======


>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b


def finish():
    game_world.clear()
    pass


def update():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    game_world.update()  # 소년과 볼 위치가 다 업데이트 완료
    game_world.handle_collisions()
=======
    game_world.update()
    # fill here

>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
    game_world.update()
    # fill here

>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
    game_world.update()
    # fill here

>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

def pause():
    pass


def resume():
    pass
=======
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
def pause():
    pass

def resume():
    pass

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
