from pico2d import *

<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)

    def get_bb(self):
        # fill here
<<<<<<< HEAD
        return 0, 0, 1600 - 1, 50
        pass
=======
        pass

>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
