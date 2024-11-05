from pico2d import load_image

from Labs.Lecture13_Game_World import game_world


class Ball:
    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.face_dir * 10)
        game_world.add_object(ball, 1)
