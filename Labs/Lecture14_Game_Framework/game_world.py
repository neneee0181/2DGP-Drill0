<<<<<<< HEAD
world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    objects = [[] for _ in range(4)]
=======
objects = [[] for _ in range(4)]
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad


def add_object(o, depth = 0):
    objects[depth].append(o)


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
<<<<<<< HEAD
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
    for layer in objects:
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
        for o in layer:
            o.draw()


def remove_object(o):
<<<<<<< HEAD
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
    for layer in objects:
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non existing object')
<<<<<<< HEAD


def clear():
    for layer in world:
        layer.clear()
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
