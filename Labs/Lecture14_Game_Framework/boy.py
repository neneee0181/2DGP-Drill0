# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
<<<<<<< HEAD

from Labs.Lecture14_Game_Framework.ball import BigBall
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
from state_machine import *
from ball import Ball
import game_world

<<<<<<< HEAD

=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
class Idle:
    @staticmethod
    def enter(boy, e):
        if start_event(e):
            boy.action = 3
            boy.face_dir = 1
        elif right_down(e) or left_up(e):
            boy.action = 2
            boy.face_dir = -1
        elif left_down(e) or right_up(e):
            boy.action = 3
            boy.face_dir = 1

        boy.frame = 0
        boy.wait_time = get_time()

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.wait_time > 2:
            boy.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


<<<<<<< HEAD
=======

>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
class Sleep:
    @staticmethod
    def enter(boy, e):
        if start_event(e):
            boy.face_dir = 1
            boy.action = 3
        boy.frame = 0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


class Run:
    @staticmethod
    def enter(boy, e):
<<<<<<< HEAD
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
            boy.dir, boy.face_dir, boy.action = -1, -1, 0

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()

<<<<<<< HEAD
=======

>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 5
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


<<<<<<< HEAD
=======



>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
class Boy:

    def __init__(self):
        self.x, self.y = 400, 90
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
                Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle}
            }
        )
<<<<<<< HEAD
        self.set_item('None')
=======
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

    def fire_ball(self):
<<<<<<< HEAD
        if self.item == 'SmallBall':
            ball = Ball(self.x, self.y, self.face_dir * 10)
            game_world.add_object(ball)
        elif self.item == 'BigBall':
            ball = BigBall(self.x, self.y, self.face_dir * 10)
            game_world.add_object(ball)

    def set_item(self, item):
        self.item = item
=======
        ball = Ball(self.x, self.y, self.face_dir * 10)
        game_world.add_object(ball)
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
