<<<<<<< HEAD
<<<<<<< HEAD
import time

=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
running = None
stack = None


def change_mode(mode):
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

<<<<<<< HEAD
<<<<<<< HEAD
    global frame_time
    frame_time = 0.0
    current_time = 0.0

=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
<<<<<<< HEAD
<<<<<<< HEAD
        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time
        print(f'Frame Time : {frame_time}, Frame Rate : {frame_rate}')
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd

    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].finish()
        stack.pop()
