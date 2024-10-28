# event ( 종류 문자열, 실제 값)
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

def space_down(e):
    return (e[0] == 'INPUT' and
    e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE)

def time_out(e):
    return e[0] == 'TIME OUT'




# 상태 머신을 처리 관리해주는 클래스
class StateMachine:
    def __init__(self, o):
        self.o = o  # boy self가 전달, self.o 상태 머신과 연결된 캐릭터 객체
        self.event_que = []  # 발생하는 이벤트를 담는 곳

        pass

    def update(self):
        self.cur_state.do(self.o)    # Idle.do()

        if self.event_que:   # list에 요소가 있으면 list 값은 true
            e = self.event_que.pop(0)   # list의 첫번째 요소를 꺼낸다
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e): # e가 check_event 이면? space_down(e)
                    self.cur_state.exit(self.o)
                    self.cur_state = next_state
                    self.cur_state.enter(self.o)
                    return



        pass

    def start(self, start_state):
        #현재 상태를 시작 상태로 만듬.
        self.cur_state = start_state
        pass

    def draw(self):
        self.cur_state.draw(self.o)
        pass

    def set_transitions(self, transitions):
        self.transitions = transitions
        pass

    def add_event(self, e):
        self.event_que.append(e)
        pass