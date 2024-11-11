#boy run speed
PIXEL_PER_METER =(10.0/0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS =(RUN_SPEED_MPS*PIXEL_PER_METER)

Time_PER_ACTION =0.5
ACTION_PER_TIME =1.0/Time_PER_ACTION
FRAME_PER_ACTION=14
import random
from ball import *
#from state_machin import StateMachine
from state_machin import *
import game_framework

class Bird:
    def __init__(self):
        self.item =None
        self.x, self.y = random.randint(0, 800), random.randint(300, 500)
        self.frame = random.randint(0, 12)
        #self.x, self.y = x,y
        #self.frame = 0
        self.dir = 1

        self.action = 1
        self.size =100;

        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Fly)
        self.state_machine.set_transitions({

        })

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT',event))
        pass

    def draw(self):
        self.state_machine.draw()

class Fly:
    @staticmethod
    def enter(boy,e):
        pass
        #boy.dir=0
        #boy.frame=0

    @staticmethod
    def exit(boy,e):

        pass
    @staticmethod
    def do(boy):
        #boy.frame = (boy.frame+1)%8
        boy.frame = (boy.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        if boy.x>1600-50:
            boy.dir=-1
        elif boy.x < 0+50:
            boy.dir = 1
    @staticmethod
    def draw(boy):
        size = boy.size
        if boy.dir==1:
            boy.image.clip_composite_draw(int(boy.frame)%5 * 180, int(boy.frame)//5 * 168, 180, 168,
                                      0,  # 90도 회전
                                      '',  # 좌우상하 반전 X
                                      boy.x, boy.y , size, size)
        else:
            boy.image.clip_composite_draw(int(boy.frame) % 5 * 180, int(boy.frame) // 5 * 168, 180, 168,
                                      0,  # 90도 회전
                                      'h',  # 좌우상하 반전 X
                                      boy.x, boy.y, size, size)

