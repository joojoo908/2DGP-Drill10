import game_framework
from pico2d import *

#import logo_mode as start_mod
import play_mod as start_mod
#import play_mod

open_canvas(1600,600)
game_framework.run(start_mod)
close_canvas()