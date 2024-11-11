from pico2d import *

<<<<<<< HEAD
<<<<<<< HEAD
from Labs.Lecture13_Game_World import game_world
=======
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


<<<<<<< HEAD
<<<<<<< HEAD
def create_world():
    global running
    global grass
    global team
    global boy

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def update_world():
    game_world.update()
=======
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
def reset_world():
    global running
    global world
    global boy

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    boy = Boy()
    world.append(boy)



def update_world():
    for o in world:
        o.update()
    pass
<<<<<<< HEAD
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb


def render_world():
    clear_canvas()
<<<<<<< HEAD
<<<<<<< HEAD
    game_world.render()
=======
    for o in world:
        o.draw()
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
    for o in world:
        o.draw()
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
    update_canvas()


open_canvas()
<<<<<<< HEAD
<<<<<<< HEAD
create_world()
=======
reset_world()
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
reset_world()
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
