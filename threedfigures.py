import math

# Cylinder
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# Cone
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# Cuboid
def cuboid_csa(l, b, h):
    return 2 * h * (l + b)

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + l*h)

def cuboid_volume(l, b, h):
    return l * b * h