from pico2d import load_image

from Labs.Lecture10_Character_Controller_1.state_machine import space_down, time_out
from state_machine import StateMachine


class Idle:
    @staticmethod
    def enter(boy):
        pass
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)
        pass



class Sleep:
    @staticmethod
    def enter(boy):
        pass
    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        pass
    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(
            boy.frame*100,300,100,100,
            3.141592/2, # 회전 각도
            '', #좌우상하 반전 X
            boy.x-25, boy.y-25, 100, 100
        )
        pass



class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)    # 어떤 객체를 위한 상태 머신인지 알려줄 필요가 있음
        self.state_machine.start(Sleep)
        self.state_machine.set_transitions(
            {
                Sleep: { space_down: Idle },
                Idle: { time_out: Sleep }
            }
        )


    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # event : input event
        # state machine event : (이벤트종류, 값)
        self.state_machine.add_event(
            ('INPUT', event)
        )

        pass

    def draw(self):
        self.state_machine.draw()