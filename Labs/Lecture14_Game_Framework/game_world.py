<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def update():
    objects = [[] for _ in range(4)]
=======
objects = [[] for _ in range(4)]
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
objects = [[] for _ in range(4)]
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
objects = [[] for _ in range(4)]
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
objects = [[] for _ in range(4)]
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b


def add_object(o, depth = 0):
    objects[depth].append(o)


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
    for layer in objects:
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
    for layer in objects:
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
    for layer in objects:
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
    for layer in objects:
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
        for o in layer:
            o.draw()


def remove_object(o):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for layer in world:
=======
    for layer in objects:
>>>>>>> 3e9d9223c1dc05e5ac3de9882257ab9311a19ceb
=======
    for layer in objects:
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
    for layer in objects:
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
    for layer in objects:
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
    for layer in objects:
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non existing object')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD


def clear():
    for layer in world:
        layer.clear()
=======
>>>>>>> 2ab3e2ba9f1fe60aeb049069248fe7de52a2e4ad
=======
>>>>>>> 5017ad4f79f2dcc517382628b1828c15b3f560dd
=======
>>>>>>> 067e7f49c5546d6fab4898d2ccb98fbb2d543732
=======
>>>>>>> 12651feccab2fd3780e9fb8f262257ced35c410b
