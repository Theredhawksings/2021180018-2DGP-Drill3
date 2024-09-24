from pico2d import *
import math




open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')


 

def draw_boy(x,y):
    boy.draw_now(x,y)


def run_top():

    for x in range(0,800,10):
        clear_canvas_now()
        draw_boy(x,550)
        delay(0.01)
        
    
def run_right():
    for y in range(550,0,-10):
        clear_canvas_now()
        draw_boy(800,y)
        delay(0.01)

    
def run_bottom():
    for x in range(800,0,-10):
        clear_canvas_now()
        draw_boy(x,0)
        delay(0.01)
   

def run_left():
    for y in range(0,550,10):
        clear_canvas_now()
        draw_boy(0,y)
        delay(0.01)




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



def run_diagonal_top_left():
    for x in range(0,400,10):
        clear_canvas_now()
        draw_boy(x,x/2*3)
        delay(0.01)

    
def run_bottom_triagnle():
    for y in range(600,0,-10):
        clear_canvas_now()
        draw_boy(400,y)
        delay(0.01)

def run_bottom_triangle():
    for x in range(400,0,-10):
        clear_canvas_now()
        draw_boy(x,0)
        delay(0.01)



def run_triagnle():
    run_diagonal_top_left()
    run_bottom_triagnle()
    run_bottom_triangle()

    



    
while(1):
    clear_canvas_now()
    run_rectangle()
    run_circle()
    run_triagnle()
    

close_canvas()
