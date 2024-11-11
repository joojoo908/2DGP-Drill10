
#0은 백그라운드 , 1은 포그라운드
world = [[],[],[],[]]

def add_object(o,depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def clear():
    for layer in world:
        layer.clear()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print("없는걸 어캐지워")