from pico2d import *
import game_world
import game_framework
import random
<<<<<<< HEAD
import server
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
<<<<<<< HEAD
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
=======
        self.image.draw(self.x, self.y)
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
<<<<<<< HEAD
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
=======
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        pass
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
