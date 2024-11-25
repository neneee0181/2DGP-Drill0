from pico2d import *
import game_world
import game_framework

<<<<<<< HEAD

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
=======
class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
<<<<<<< HEAD
        draw_rectangle(*self.get_bb())
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        # fill here
<<<<<<< HEAD
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
        pass

    def handle_collision(self, group, other):
        # fill here
<<<<<<< HEAD
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass
=======
        pass
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
