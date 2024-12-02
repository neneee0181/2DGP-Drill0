from pico2d import *

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
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
<<<<<<< HEAD
<<<<<<< HEAD
        return 0, 0, 1600 - 1, 50
        pass
=======
        pass

>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
        pass

>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
        pass

>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
