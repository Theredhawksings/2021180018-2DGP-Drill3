from pico2d import *
import math




open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_top():
    pass
    
def run_right():
    pass
    
def run_bottom():
    pass

def run_left():
    pass



def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass


def run_circle():
    rad=300

    cx=800//2
    cy=600//2

    r=300
    
    for i in range(0, 360):
        
        x=r*math.cos(math.radians(i))+cx
        y=r*math.sin(math.radians(i))+cy
    
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)


while(1):
    clear_canvas_now()
    run_rectangle()
    run_circle()
    break

close_canvas()
