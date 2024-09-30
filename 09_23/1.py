from pico2d import *

open_canvas()
hide_lattice()  # 모눈 종이 사라짐
# show_lattice() # 모눈 종이 생김
# close_canvas() # 종료
img = load_image("character.png")
img.draw_now(400, 300)
img.draw_now(500,400)
clear_canvas_now()

for x in range(0,9):
    for y in range(0,7):
        img.draw_now(x*100,y*100)
