world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    objects = [[] for _ in range(4)]


def add_object(o, depth = 0):
    objects[depth].append(o)


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
        for o in layer:
            o.draw()


def remove_object(o):
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in world:
        layer.clear()