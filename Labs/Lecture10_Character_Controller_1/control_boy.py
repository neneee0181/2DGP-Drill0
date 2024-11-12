from pico2d import *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from Labs.Lecture10_Character_Controller_1.Boy import Boy
from Labs.Lecture10_Character_Controller_1.grass import Grass
=======
=======
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
import random


# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
=======
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                boy.handle_event(event)
=======
            boy.handle_event(event)
>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
=======
            boy.handle_event(event)
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
            boy.handle_event(event)
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
            boy.handle_event(event)
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad


def reset_world():
    global running
    global grass
    global team
    global world
    global boy

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    boy = Boy()
    world.append(boy)


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
=======

>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======

>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======

>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
