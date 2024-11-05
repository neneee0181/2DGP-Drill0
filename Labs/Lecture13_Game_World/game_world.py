# layer 0 : Background Objects
# layer 1 : Foreground Objects

world = [[], []]


def add_object(o, depth=0):
    world[depth].append(o)


def add_objects(ol, depth=0):
    world[depth].append(ol)


def update():
    for layer in world:
        for o in world:
            o.update()


def render():
    for layer in world:
        for o in world:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in world:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
