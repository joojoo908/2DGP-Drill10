import game_framework
from pico2d import*
import play_mod
from pygame.examples.cursors import image


def init():
    global image
    global logo_start_time

    image = load_image('title.png')

    logo_start_time=get_time()

def finish():
    global image
    del image

def update():
    # global logo_start_time
    # if get_time() -logo_start_time >2.0:
    #     logo_start_time =get_time()
    #     game_framework.quit()
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events =get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) ==(SDL_KEYDOWN,SDLK_SPACE):
            game_framework.change_mode(play_mod)