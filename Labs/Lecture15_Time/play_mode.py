from pico2d import *
import game_framework

import game_world
from grass import Grass
<<<<<<< HEAD
from bird import Boy

=======
from boy import Boy
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad

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
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
def init():
    global grass
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
<<<<<<< HEAD
    # 성능이 후진 컴터
    # delay(0.5)

=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad

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

>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
