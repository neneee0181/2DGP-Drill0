import turtle

def move(direction):
    if direction == 'left':
        turtle.setheading(180)  # 왼쪽 방향으로 회전
        turtle.forward(50)
    elif direction == 'right':
        turtle.setheading(0)  # 오른쪽 방향으로 회전
        turtle.forward(50)
    elif direction == 'up':
        turtle.setheading(90)  # 위쪽 방향으로 회전
        turtle.forward(50)
    elif direction == 'down':
        turtle.setheading(270)  # 아래쪽 방향으로 회전
        turtle.forward(50)

    turtle.stamp()

turtle.shape('turtle')

turtle.listen()
turtle.onkey(lambda: move('left'), 'Left')
turtle.onkey(lambda: move('right'), 'Right')
turtle.onkey(lambda: move('up'), 'Up')
turtle.onkey(lambda: move('down'), 'Down')

turtle.onkey(lambda: turtle.reset(), 'Escape')

