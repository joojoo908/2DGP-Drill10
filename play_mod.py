from pico2d import *
import game_framework
import title_mod
import item_mod
from grass import Grass
from boy import Boy
from bird import Bird
import game_world

# 클래스 단위로 분리
# Game object class here

#event_boy=0
def handle_events():
    global running
    #global event_boy
    events = get_events()
    for event in events:
        #if event.type==SDL_KEYDOWN:
            #if event.key ==SDLK_RIGHT:
                #event_boy=1

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mod)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mod)
        else:
            boy.handle_event(event)

def init():
    global running
    global grass
    global team
    global world
    global boy

    running = True
    world = []

    # grass = Grass(400,80)
    # game_world.add_object(grass,0)
    grass = Grass(400,30)
    game_world.add_object(grass,0)

    boy = Boy()
    game_world.add_object(boy,1)

    bird =Bird(1000,500)
    game_world.add_object(bird,1)

    # grass = Grass(400, 30)
    # game_world.add_object(grass, 1)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass





