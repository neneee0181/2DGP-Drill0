from pico2d import *
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90  #random 함수가 반복문 수만큼 호출
        self.frame = 0
        if Boy.image is None:
            Boy.image = load_image('run_animation.png') # 이미지를 반복문 수 만큼 호출하기 때문에 문제가 됨 (객체기 때문에 메모리에 낭비하게됨) # 정적으로 해주면됨
        
=======
=======
>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
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
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 28126e585c4bf95e61a8c4fec11346bca046c983
=======
>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
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
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team


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
    delay(0.05)
# finalization code
close_canvas()
