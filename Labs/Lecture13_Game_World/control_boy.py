from pico2d import *

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from Labs.Lecture13_Game_World import game_world
=======
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
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
<<<<<<< HEAD
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
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732


def render_world():
    clear_canvas()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    for o in world:
        o.draw()
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
    for o in world:
        o.draw()
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
    for o in world:
        o.draw()
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
    update_canvas()


open_canvas()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
create_world()
=======
reset_world()
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
reset_world()
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
reset_world()
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
reset_world()
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
reset_world()
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
