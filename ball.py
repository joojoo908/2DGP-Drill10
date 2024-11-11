from pico2d import load_image

import game_world


class Ball:
    image =None
    def __init__(self,x,y,velocity):
        if Ball.image ==None:
            self.image = load_image('ball21x21.png')
        self.x,self.y,self.velocity =x,y,velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x+=self.velocity*10;
        if self.x <25 or self.x>800-25:
            game_world.remove_object(self)

class BigBall:
    image =None
    def __init__(self,x,y,velocity):
        if Ball.image ==None:
            self.image = load_image('ball41x41.png')
        self.x,self.y,self.velocity =x,y,velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x+=self.velocity*10;
        if self.x <25 or self.x>800-25:
            game_world.remove_object(self)