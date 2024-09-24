from pico2d import *

import math




open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')



def run_rectangle():
    pass


def run_circle():
    clear_canvas_now()
    boy.draw_now(400,90)
    delay(0.01)
    pass

    

while(1):
    clear_canvas_now()
    run_rectangle()
    run_circle()
    break

close_canvas()
