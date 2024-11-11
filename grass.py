from pico2d import load_image

class Grass:
    def __init__(self,x,y):
        self.x ,self.y = x,y
        self.image = load_image('grass.png')
        self.ruler_image = load_image('ruler.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x+800, self.y)
        self.ruler_image.draw(800, 350)

    def update(self):
        pass
