from pico2d import *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random

class Ball:
    def __init__(self, image, x, y, fall_speed):
        self.image = load_image(image)
        self.x = x
        self.y = y
        self.fall_speed = fall_speed
        self.ground_level = 0 if '21x21' in image else 0

    def update(self):
        if self.y > self.ground_level:
            self.y -= self.fall_speed
            if self.y < self.ground_level:
                self.y = self.ground_level

    def draw(self):
        self.image.draw(self.x, self.y)
=======

# Game object class here
>>>>>>> 6cb1cb5eaedcd79e9ca86a683e1df8c5b8a91b55
=======

# Game object class here
>>>>>>> 6cb1cb5eaedcd79e9ca86a683e1df8c5b8a91b55
=======

# Game object class here
>>>>>>> 28126e585c4bf95e61a8c4fec11346bca046c983
=======

# Game object class here
>>>>>>> 2a1e9505020fe82bfec1d2f4fd9632625922596c
=======

# Game object class here
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======

# Game object class here
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======

# Game object class here
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======

# Game object class here
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======

# Game object class here
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======

# Game object class here
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
balls = []
for i in range(20):
    x = random.randint(0, 800)
    y = 599
    fall_speed = random.uniform(2, 10)
    if random.randint(0, 1) == 0:
        balls.append(Ball('ball21x21.png', x, y, fall_speed))
    else:
        balls.append(Ball('ball41x41.png', x, y, fall_speed))

running = True

while running:
    handle_events()

    for ball in balls:
        ball.update()

    clear_canvas()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.03)

close_canvas()
=======
=======
>>>>>>> 6cb1cb5eaedcd79e9ca86a683e1df8c5b8a91b55
=======
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
# initialization code

# game main loop code

# finalization code

close_canvas()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb1cb5eaedcd79e9ca86a683e1df8c5b8a91b55
=======
>>>>>>> 6cb1cb5eaedcd79e9ca86a683e1df8c5b8a91b55
=======
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
