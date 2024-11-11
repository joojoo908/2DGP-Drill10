import game_framework
from pico2d import *

import game_world
import play_mod
from pannel import Pannel

def init():
    global pannel
    pannel =Pannel()
    game_world.add_object(pannel,3)

def finish():
    game_world.remove_object(pannel)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update():
    pass

def handle_events():
    global running
    #global event_boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mod.boy.set_item ('None')
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mod.boy.set_item ('Ball')
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mod.boy.set_item ('BigBall')
            game_framework.pop_mode()

def pause():
    pass

def resume():
    pass