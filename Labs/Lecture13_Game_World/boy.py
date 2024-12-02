# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from state_machine import *


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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if space_down(e):
            boy.fire_ball()
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
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.wait_time > 2:
            boy.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir, boy.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
            boy.dir, boy.face_dir, boy.action = -1, -1, 0

    @staticmethod
    def exit(boy, e):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if space_down(e):
            boy.fire_ball()
        pass

=======
        pass


>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
        pass


>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
        pass


>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
        pass


>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
        pass


>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
        pass


>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 5
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
class Boy:

    def __init__(self):
        self.x, self.y = 400, 90
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Idle},
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> d1656090229e5b969c2b1c9b4ef5a19813bfe3e4
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
                Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, space_down: Idle}
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def fire_ball(self):
        if self.face_dir == -1:
            print('FIRE BALL LEFT')
        elif self.face_dir == 1:
            print('FIRE BALL RIGHT')
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
